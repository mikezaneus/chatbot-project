variable "project_id" {
  description = "The GCP project ID"
  type        = string
}

variable "region" {
  description = "The GCP region to deploy to"
  type        = string
}

variable "env" {
  description = "Deployment environment (e.g., dev, staging, prod)"
  type        = string
}

variable "version" {
  description = "The image version to deploy"
  type        = string
}

variable "teams_webhook" {
  description = "Microsoft Teams Webhook URL"
  type        = string
  default = null
}

variable "sendgrid_api_key" {
  description = "SendGrid API key"
  type        = string
  default     = null
}

variable "alert_email" {
  description = "Alert recipient email address"
  type        = string
}

variable "bucket_name" {
  description = "Cloud Storage bucket for audit reports"
  type        = string
}


