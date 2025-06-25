variable "project_id" {
  type        = string
  description = "GCP project ID"
}

variable "region" {
  type        = string
  default     = "us-central1"
  description = "GCP region"
}

variable "image_url" {
  type        = string
  description = "Docker image URL for Cloud Run deployment"
}

variable "service_account_id" {
  type        = string
  description = "Service account ID for the Cloud Run service"
}