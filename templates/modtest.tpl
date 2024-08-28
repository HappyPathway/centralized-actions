name: "ModTest"

on:
  pull_request:
    branches:
      - main
    
jobs:
  modtest:
    uses: HappyPathway/centralized-actions/.github/workflows/modtest.yml@main
    with:
       workspace: ${workspace}
       github_server: ${github_server} 
       github_org: ${github_org}
       mod_source: ${mod_source}
       branch: ${{ github.head_ref }}
       terraform_version: ${terraform_version}
    secrets:
      TFE_TOKEN: ${{ secrets.TFE_TOKEN }}
      GH_TOKEN: ${{ secrets.GH_TOKEN }}