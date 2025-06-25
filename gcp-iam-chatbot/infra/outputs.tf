output "cloud_run_url" {
  value = google_cloud_run_service.chatbot.status[0].url
}

output "pubsub_topic" {
  value = google_pubsub_topic.alerts.name
}

output "log_bucket" {
  value = google_storage_bucket.logs.name
}