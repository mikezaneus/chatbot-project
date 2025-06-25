from google.cloud import recommender_v1

def get_iam_recommendations(project_id):
    client = recommender_v1.RecommenderClient()
    parent = f"projects/{project_id}/locations/global/recommenders/google.iam.policy.Recommender"
    recommendations = client.list_recommendations(parent=parent)
    return [rec.name for rec in recommendations]