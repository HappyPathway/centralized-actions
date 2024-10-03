# centralized-actions
## terraform-test:
```yaml
name: "Gtag"

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

  gtag:
    if: github.ref == 'refs/heads/main' && github.event_name != 'pull_request'
    needs: terraform
    uses: HappyPathway/centralized-actions/.github/workflows/gtag.yml@main
    with:
      patch: true
      github_org: ${{ vars.GH_ORG }}
      github_username: ${{ vars.GH_USERNAME }}
      github_email: ${{ vars.GH_EMAIL }}
    secrets:
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
