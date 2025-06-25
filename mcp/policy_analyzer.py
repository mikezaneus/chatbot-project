from google.cloud import asset_v1

def analyze_iam_policy(scope, full_resource_name):
    client = asset_v1.AssetServiceClient()
    analysis_request = asset_v1.AnalyzeIamPolicyRequest(
        analysis_query=asset_v1.IamPolicyAnalysisQuery(
            scope=scope,
            resource_selector=asset_v1.IamPolicyAnalysisQuery.ResourceSelector(
                full_resource_name=full_resource_name
            )
        )
    )
    response = client.analyze_iam_policy(request=analysis_request)
    return [result for result in response.main_analysis.analysis_results]