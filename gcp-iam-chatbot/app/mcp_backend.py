import os
import json
from flask import Flask, request, jsonify
from google.cloud import iam_v1, storage

app = Flask(__name__)

PROJECT_ID = os.getenv("GCP_PROJECT")
BUCKET_NAME = os.getenv("BUCKET_NAME")

@app.route("/analyze_roles", methods=["GET"])
def analyze_roles():
    client = iam_v1.IAMClient()
    org_name = f"organizations/{PROJECT_ID}"
    response = client.query_grantable_roles(request={"full_resource_name": f"//cloudresourcemanager.googleapis.com/projects/{PROJECT_ID}"})

    risky_roles = []
    for role in response.roles:
        risky_perms = [p for p in role.included_permissions if "delete" in p or "admin" in p]
        if risky_perms:
            risky_roles.append({
                "role": role.name,
                "title": role.title,
                "risky_permissions": risky_perms
            })

    _write_to_gcs(risky_roles)
    return jsonify(risky_roles)

def _write_to_gcs(data):
    storage_client = storage.Client()
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(f"iam_analysis_{PROJECT_ID}.json")
    blob.upload_from_string(json.dumps(data, indent=2), content_type="application/json")

@app.route("/")
def health():
    return "IAM Chatbot API is running", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)