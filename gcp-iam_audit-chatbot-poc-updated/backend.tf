
terraform {
  backend "gcs" {
    bucket  = "your-tf-state-bucket"
    prefix  = "iam-chatbot/state"
  }
}
