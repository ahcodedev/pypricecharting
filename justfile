# List available recipes
[private]
default:
    @just --list
# Build the sdist and wheel into dist/
build:
    uv build
# Check dependencies for known vulnerabilities (pip-audit)
audit:
    uv run pip-audit --skip-editable
# Scan staged changes for secrets
betterleaks:
    betterleaks git --pre-commit --staged --redact
# Type check, lint, format check, and lint workflows, YAML, and JSON without changing files
ci-lint:
    uv run ty check
    uv run ruff check .
    uv run ruff format --check .
    actionlint .github/workflows/*.yml
    yamllint --strict .
    just json-lint
# Run unit tests with coverage (fails under 98%)
coverage:
    uv run pytest --cov
# Build the docs in strict mode (output in site/)
docs-build:
    uv run zensical build --strict
# Serve the docs locally with live reload
docs-serve:
    uv run zensical serve
# Validate JSON files (devcontainer.json is skipped because it allows comments)
json-lint:
    find . -name '*.json' -not -path './.venv/*' -not -name devcontainer.json -exec jq empty {} +
# Type check, lint, format, spell check, and lint workflows, YAML, and JSON, applying fixes
lint:
    uv run ty check
    uv run ruff check . --fix
    uv run ruff format .
    typos --write-changes
    actionlint .github/workflows/*.yml
    yamllint --strict .
    just json-lint
# Lint Markdown files
markdownlint:
    markdownlint-cli2 "**/*.md"
# Run the git hooks on staged files
prek:
    uv run prek
# Remove non-release default labels and sync the release labels on GitHub
set-github-labels:
    ./scripts/sync-labels.sh
# Install Homebrew tools and sync the project
setup:
    brew bundle install
    uv run prek install
    just sync
# Check spelling
spellcheck:
    typos
# Install all dependency groups into .venv
sync:
    uv sync --all-groups
# Run unit tests
test:
    uv run pytest
# Pull in the latest changes from the Copier template
update-template:
    copier update --trust
# Audit GitHub Actions workflows for security issues
zizmor:
    zizmor . --collect all
