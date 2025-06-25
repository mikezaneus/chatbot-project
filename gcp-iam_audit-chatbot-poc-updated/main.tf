provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_cloud_run_service" "iam_chatbot" {
  name     = "iam-chatbot-${var.env}"
  location = var.region

  template {
    spec {
      containers {
        image = "gcr.io/${var.project_id}/iam-chatbot:${var.version}"

        env {
          name  = "ENV"
          value = var.env
        }

        env {
          name  = "GCP_PROJECT"
          value = var.project_id
        }

        env {
          name  = "TEAMS_WEBHOOK"
          value = var.teams_webhook
        }

        env {
          name  = "SENDGRID_API_KEY"
          value = var.sendgrid_api_key
        }

        env {
          name  = "ALERT_EMAIL"
          value = var.alert_email
        }

        env {
          name  = "BUCKET_NAME"
          value = var.bucket_name
        }
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }

  metadata {
    annotations = {
      "run.googleapis.com/ingress"        = "all"
      "run.googleapis.com/launch-stage"   = "BETA"
    }
  }
}

