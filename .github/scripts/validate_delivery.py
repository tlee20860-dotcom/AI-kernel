name: Kernel Commit Validation
on:
  push:
    paths:
      - 'docs/**/*.md'
      - 'docs/**/*.json'
      - 'docs/**/*.txt'

jobs:
  call-validation:
    uses: tlee20860-dotcom/AI-infra/.github/workflows/validate.yml@main
    secrets:
      CROSS_REPO_PAT: ${{ secrets.CROSS_REPO_PAT }}

# ═══ EOF ═══
# F: AI-kernel/.github/workflows/validate.yml
# V: 1792906000
# W: ai-system-003#9
# ═══ EOF ═══