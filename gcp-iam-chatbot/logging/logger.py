import logging
import os

log_file = os.getenv("LOG_FILE", "iam_chatbot.log")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def log_event(event):
    logging.info(event)