from google.cloud import storage
import datetime
import os

def log_to_gcs(bucket_name, log_message):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    timestamp = datetime.datetime.utcnow().isoformat()
    blob = bucket.blob(f"logs/{timestamp}.log")
    blob.upload_from_string(log_message)
    return f"Logged to {blob.name}"