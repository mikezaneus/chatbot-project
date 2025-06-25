
terraform {
  backend "gcs" {
    bucket  = "iam-audit-project-2025"
    prefix  = "iam-chatbot/state"
  }
}
