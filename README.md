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
## modtest
```yaml
name: "ModTest"

on:
  pull_request:
    branches:
      - main
    
jobs:
  modtest:
    uses: HappyPathway/centralized-actions/.github/workflows/modtest.yml@main
    with:
       workspace: github-repos
       github_server: github.com 
       github_org:  ${{ github.repository_owner }} 
       mod_source: repo/github
       branch: ${{ github.head_ref }}
       terraform_version: 1.9.1
    secrets:
      TFE_TOKEN: ${{ secrets.TFE_TOKEN }}
      GH_TOKEN: ${{ secrets.GH_TOKEN }}
```