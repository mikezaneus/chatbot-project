Feature: IAM Policy Audit

  Scenario: Ensure custom roles do not allow dangerous permissions
    Given I have a role definition with "iam.serviceAccounts.actAs"
    When I evaluate the policy with OPA
    Then I should see a denial reason