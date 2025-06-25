
import os
import json
import logging
from datetime import datetime
from google.cloud import storage
from googleapiclient.discovery import build
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail
import requests

# Environment variables
PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT") 
BUCKET_NAME = os.getenv("BUCKET_NAME")
# SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
# ALERT_EMAIL = os.getenv("ALERT_EMAIL")
# FROM_EMAIL = os.getenv("FROM_EMAIL", "security-alerts@yourdomain.com")
# TEAMS_WEBHOOK = os.getenv("TEAMS_WEBHOOK")

# Define keywords that indicate risky permissions
RISKY_KEYWORDS = ["delete", "admin", "setIamPolicy", "impersonate", "update"]

def get_custom_roles():
    service = build('iam', 'v1')
    roles = service.organizations().roles().list(parent=f"organizations/{PROJECT_ID}").execute()
    return roles.get("roles", [])

def get_risky_permissions(role):
    return [perm for perm in role.get("includedPermissions", []) if any(keyword in perm for keyword in RISKY_KEYWORDS)]

def write_to_gcs(report_data):
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H-%M-%SZ')
    blob = bucket.blob(f"iam_audit_report_{PROJECT_ID}_{timestamp}.json")
    blob.upload_from_string(json.dumps(report_data, indent=2), content_type='application/json')

# def send_email_alert(alert_data):
#     message = Mail(
#         from_email=FROM_EMAIL,
#         to_emails=ALERT_EMAIL,
#         subject='🚨 GCP IAM Audit Alert: Risky Permissions Detected',
#         html_content=f"<pre>{json.dumps(alert_data, indent=2)}</pre>"
#     )
    # try:
    #     sg = SendGridAPIClient(SENDGRID_API_KEY)
    #     sg.send(message)
    # except Exception as e:
    #     logging.error(f"Failed to send alert email: {str(e)}")

# def send_teams_alert(alert_data):
#     if not TEAMS_WEBHOOK:
#         logging.warning("TEAMS_WEBHOOK not set. Skipping Teams alert.")
#         return

#     headers = {'Content-Type': 'application/json'}
#     message = {
#         "@type": "MessageCard",
#         "@context": "http://schema.org/extensions",
#         "summary": "GCP IAM Audit Alert",
#         "themeColor": "EA4300",
#         "title": "🚨 Risky Permissions Detected",
#         "text": f"Some custom roles contain risky permissions:\n\n<pre>{json.dumps(alert_data, indent=2)}</pre>"
#     }

    # try:
    #     requests.post(TEAMS_WEBHOOK, headers=headers, json=message)
    # except Exception as e:
    #     logging.error(f"Failed to send Teams alert: {str(e)}")

def main(request):
    report = {}
    risky_roles = []

    roles = get_custom_roles()
    for role in roles:
        role_name = role["name"]
        risky = get_risky_permissions(role)
        report[role_name] = {
            "title": role.get("title"),
            "permissions": role.get("includedPermissions", []),
            "risky_permissions": risky
        }
        if risky:
            risky_roles.append({"role": role_name, "risky_permissions": risky})

    write_to_gcs(report)

    if risky_roles:
        send_email_alert(risky_roles)
        send_teams_alert(risky_roles)

    return ("IAM audit completed successfully.", 200)


