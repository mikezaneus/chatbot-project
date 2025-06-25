from google.cloud import pubsub_v1
import os

def publish_alert(topic_id, message):
    project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)
    future = publisher.publish(topic_path, message.encode("utf-8"))
    return future.result()