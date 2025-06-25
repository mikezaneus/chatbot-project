# Microsoft Teams Bot Integration for Vertex AI Agent

## Steps to Integrate Vertex AI Chatbot with Microsoft Teams

1. **Create Azure Bot Resource**
   - Go to Azure Portal
   - Create a new "Azure Bot" under "Bot Services"
   - Set messaging endpoint to your deployed Cloud Run URL or webhook endpoint

2. **Register Microsoft Teams Channel**
   - In Azure Bot resource, go to Channels
   - Add Microsoft Teams
   - Accept terms and configure Teams settings

3. **Configure Teams App Manifest**
   - Create a Teams app package
   - Include bot ID, name, endpoint, and icons
   - Upload to Teams Admin Center for distribution

4. **Connect from Vertex AI Agent**
   - In Vertex AI Agent Builder, set the fulfillment webhook to your MCP backend
   - Ensure CORS and authentication are configured if necessary

## References
- https://learn.microsoft.com/en-us/microsoftteams/platform/bots/what-are-bots
- https://cloud.google.com/vertex-ai/docs/agents