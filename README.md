# centralized-actions
## terraform-test:
```yaml
name: "Terraform"

on:
  workflow_dispatch:
  pull_request:
    
jobs:
  terraform:
    uses: HappyPathway/centralized-actions/.github/workflows/terraform-test.yml@main
    with:
      terraform_version: ${{ vars.terraform_version }}
      terraform_api: ${{ vars.terraform_api }}
      github_username: ${{ github.actor }}
      github_email: ${{ github.actor }}@roknsound.com
      github_org: ${{ github.repository_owner }} 
    secrets:
      TFE_TOKEN: ${{ secrets.TFE_TOKEN }}
      GH_TOKEN: ${{ secrets.GH_TOKEN }}
```
