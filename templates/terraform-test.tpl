name: "Terraform"

on:
  workflow_dispatch:
  pull_request:
    
jobs:
  terraform:
    uses: HappyPathway/centralized-actions/.github/workflows/terraform-test.yml@main
    with:
      terraform_version: $${{ vars.terraform_version }}
      terraform_api: $${{ vars.terraform_api }}
      github_username: ${github_username}
      github_email: ${github_email}
      github_org: $${{ github.repository_owner }} 
    secrets:
      TFE_TOKEN: ${{ secrets.TFE_TOKEN }}
      GH_TOKEN: ${{ secrets.GH_TOKEN }}