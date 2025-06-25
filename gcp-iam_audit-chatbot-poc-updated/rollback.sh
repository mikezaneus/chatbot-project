!/bin/bash
Rollback IAM Chatbot to a previous Docker image version

set -e

if [ -z "$1" ]; then
  echo "❗ Usage: ./rollback.sh <previous_version_number>"
  exit 1
fi

VERSION=$1
SERVICE="iam-chatbot"
REGION="us-central1"
PROJECT_ID=$(gcloud config get-value project)
IMAGE="gcr.io/${PROJECT_ID}/${SERVICE}:${VERSION}"

echo "🔁 Rolling back ${SERVICE} to version: ${VERSION}"
echo "🔍 Using image: ${IMAGE}"

# Confirm the image exists
if ! gcloud container images describe "${IMAGE}" >/dev/null 2>&1; then
  echo "❌ Error: Image ${IMAGE} not found in GCR. Aborting."
  exit 1
fi

# Deploy the old version
gcloud run deploy "${SERVICE}" \
  --image "${IMAGE}" \
  --platform managed \
  --region "${REGION}" \
  --allow-unauthenticated

echo "✅ Successfully rolled back to version: ${VERSION}"


