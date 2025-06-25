import requests
import json

def send_teams_alert(webhook_url, title, text):
    message = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "summary": title,
        "themeColor": "0076D7",
        "title": title,
        "text": text
    }
    response = requests.post(webhook_url, data=json.dumps(message),
                             headers={"Content-Type": "application/json"})
    return response.status_code == 200