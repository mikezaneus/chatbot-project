# GCP IAM Chatbot with Vertex AI, Terraform, and GitHub Actions

## 🔧 Overview

This project deploys a GCP-native IAM chatbot using:
- Vertex AI + Agent Builder (LLM front-end)
- Flask MCP backend (Cloud Run)
- GCP IAM APIs: Recommender, Policy Analyzer, Troubleshooter
- GCS logging, Pub/Sub alerts, Teams webhooks
- Full Terraform infrastructure
- GitHub Actions CI/CD pipeline

---

## 📁 Directory Structure

```
gcp-iam-chatbot/
├── app.py                   # Flask MCP server
├── mcp/                     # API integration modules
├── deploy/                  # Deployment scripts & Teams setup
├── infra/                   # Terraform IaC
├── tests/                   # Behave test framework
├── notify/, logging/        # Alerting & logging modules
├── docs/                    # Design docs
```

---

## 🚀 Deployment Instructions

### 1. Setup Prerequisites

- A GCP Project with billing enabled
- Enable APIs:
  - Cloud Run, IAM, Recommender, Asset Inventory, Pub/Sub, Vertex AI
```bash
gcloud services enable run.googleapis.com recommender.googleapis.com   iam.googleapis.com cloudasset.googleapis.com pubsub.googleapis.com   policytroubleshooter.googleapis.com
```

---

### 2. Terraform Setup

```bash
cd gcp-iam-chatbot/infra

export TF_VAR_project_id="your-project-id"
export TF_VAR_region="us-central1"
export TF_VAR_image_url="gcr.io/your-project/iam-chatbot"

terraform init
terraform apply
```

---

### 3. Build & Push Docker Image

```bash
gcloud builds submit --tag gcr.io/your-project/iam-chatbot
```

This image URL is used in Terraform input variable `image_url`.

---

### 4. GitHub Actions CI/CD

#### Secrets Required

| Secret Name | Value |
|-------------|-------|
| `GOOGLE_CREDENTIALS` | Base64-encoded GCP service account JSON |
| `TF_VAR_project_id` | GCP project ID |
| `TF_VAR_region` | e.g. `us-central1` |
| `TF_VAR_image_url` | Docker image: `gcr.io/your-project/iam-chatbot` |

---

### 5. Microsoft Teams Integration

1. Register bot in Azure
2. Add Teams channel
3. Set endpoint to Cloud Run URL
4. Configure manifest in Teams Admin Center

See `deploy/teams_bot_setup.md` for details.

---

### 6. Test the Chatbot

```bash
curl https://your-cloud-run-url/recommendations?project_id=your-project-id
```

---

### 7. Log & Alert

- Logs sent to GCS bucket `${project}-iam-logs`
- Alerts published to Pub/Sub topic `iam-chatbot-alerts`
- Optional: send alerts via `teams_webhook.py` or `email_alert.py`

---

## 📎 References

- [IAM Recommender](https://cloud.google.com/recommender/docs/iam-policy)
- [Policy Analyzer](https://cloud.google.com/asset-inventory/docs/analyzing-policies)
- [Vertex AI Agents](https://cloud.google.com/vertex-ai/docs/agents)
- [Teams Bots](https://learn.microsoft.com/en-us/microsoftteams/platform/bots/what-are-bots)

---