from google.cloud import policytroubleshooter_v1

def troubleshoot_iam(principal, full_resource_name, permission):
    client = policytroubleshooter_v1.IamCheckerClient()
    access_tuple = policytroubleshooter_v1.AccessTuple(
        principal=principal,
        full_resource_name=full_resource_name,
        permission=permission
    )
    response = client.troubleshoot_iam_policy(request={"access_tuple": access_tuple})
    return {
        "access": response.access.name,
        "explained_policies": [policy.policy for policy in response.explained_policies]
    }