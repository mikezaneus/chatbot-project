# SendGrid Secret
resource "google_secret_manager_secret" "sendgrid_api_key" {
  secret_id = "sendgrid-api-key"
  replication {
    automatic = true
  }
}

resource "google_secret_manager_secret_version" "sendgrid_api_key_version" {
  secret      = google_secret_manager_secret.sendgrid_api_key.id
  secret_data = var.sendgrid_api_key
}

# Microsoft Teams Webhook Secret
resource "google_secret_manager_secret" "teams_webhook_url" {
  secret_id = "teams-webhook-url"
  replication {
    automatic = true
  }
}

resource "google_secret_manager_secret_version" "teams_webhook_url_version" {
  secret      = google_secret_manager_secret.teams_webhook_url.id
  secret_data = var.teams_webhook_url
}


