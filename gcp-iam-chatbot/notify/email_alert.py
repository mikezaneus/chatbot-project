import smtplib
from email.message import EmailMessage

def send_alert(subject, body, to_email):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = "noreply@yourdomain.com"
    msg["To"] = to_email

    with smtplib.SMTP("smtp.yourdomain.com") as server:
        server.send_message(msg)