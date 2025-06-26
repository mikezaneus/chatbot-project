package gcp.audit

deny[reason] {
  input.role.included_permissions[_] == perm
  perm == "iam.serviceAccounts.actAs"
  reason := "Use of actAs permission is restricted"
}

deny[reason] {
  input.role.included_permissions[_] == perm
  startswith(perm, "resourcemanager.") 
  contains(perm, "delete")
  reason := "Role includes delete on resourcemanager"
}