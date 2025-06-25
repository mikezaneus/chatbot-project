terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = ">= 4.0"
    }
  }
  required_version = ">= 1.3.0"
}

provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_storage_bucket" "logs" {
  name     = "${var.project_id}-iam-logs"
  location = var.region
  uniform_bucket_level_access = true
  force_destroy = true
}

resource "google_pubsub_topic" "alerts" {
  name = "iam-chatbot-alerts"
}

resource "google_service_account" "chatbot" {
  account_id   = var.service_account_id
  display_name = "IAM Chatbot Service Account"
}

resource "google_cloud_run_service" "chatbot" {
  name     = "iam-chatbot"
  location = var.region

  template {
    spec {
      containers {
        image = var.image_url
      }
      service_account_name = google_service_account.chatbot.email
    }
  }

  traffics {
    percent         = 100
    latest_revision = true
  }

  autogenerate_revision_name = true
}

resource "google_cloud_run_service_iam_member" "invoker" {
  location        = google_cloud_run_service.chatbot.location
  service         = google_cloud_run_service.chatbot.name
  role            = "roles/run.invoker"
  member          = "allUsers"
}