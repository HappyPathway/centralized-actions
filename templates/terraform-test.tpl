name: "Terraform Test"

on:
  workflow_dispatch:
  pull_request:
  push:
    branches:
      - main
    
jobs:
  terraform:
    uses: HappyPathway/centralized-actions/.github/workflows/terraform-test.yml@main
    with:
      terraform_version: ${{vars.TERRAFORM_VERSION}}
      terraform_api: ${{vars.TERRAFORM_API}}
      terraform_init: true
      github_username: ${{vars.GH_USERNAME}}
      github_email: ${{vars.GH_EMAIL}}
      github_org: ${{ vars.GH_ORG }}
      download_cache: false
    secrets:
      TFE_TOKEN: ${{ secrets.TFE_TOKEN }}
      GH_TOKEN: ${{ secrets.GH_TOKEN }}
