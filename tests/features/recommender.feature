Feature: IAM Role Recommendation
  Scenario: Fetch IAM recommendations for a GCP project
    Given the project id is "test-project"
    When I call the recommendations endpoint
    Then I should receive a list of IAM recommendations