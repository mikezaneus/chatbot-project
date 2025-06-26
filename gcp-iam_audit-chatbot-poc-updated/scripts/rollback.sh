#!/bin/bash
if [ -z "$1" ]; then
  echo "Usage: ./rollback.sh <version>"
  exit 1
fi

VERSION=$1
PROJECT_ID=$(gcloud config get-value project)
IMAGE="gcr.io/${PROJECT_ID}/iam-chatbot:${VERSION}"

gcloud run deploy iam-chatbot \
  --image $IMAGE \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated

echo "✅ Rolled back to version $VERSION"