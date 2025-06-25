#!/bin/bash
gcloud builds submit --tag gcr.io/$(gcloud config get-value project)/iam-chatbot
gcloud run deploy iam-chatbot --image gcr.io/$(gcloud config get-value project)/iam-chatbot --platform managed --allow-unauthenticated