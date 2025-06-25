from behave import given, when, then
import requests

@given('the project id is "{project_id}"')
def step_given_project_id(context, project_id):
    context.project_id = project_id

@when("I call the recommendations endpoint")
def step_call_recommendations(context):
    response = requests.get(f"http://localhost:5000/recommendations?project_id={context.project_id}")
    context.response = response

@then("I should receive a list of IAM recommendations")
def step_check_response(context):
    assert context.response.status_code == 200
    assert isinstance(context.response.json(), list)