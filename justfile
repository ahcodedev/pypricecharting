[private]
list:
    @just --list
# Build the sdist and wheel into dist/
build:
    uv build
# Lint without modifying files
ci-lint:
    uv run ty check
    uv run ruff check .
    uv run ruff format --check .
    uv run codespell
# Serve the docs site with live reload
docs:
    uv run zensical serve
# Build the docs site in strict mode
docs-build:
    uv run zensical build --strict
# Scan staged changes for secrets
git-leaks:
    gitleaks git --pre-commit --staged --redact
# Type check, lint, format and spellcheck, fixing files in place
lint:
    uv run ty check
    uv run ruff check . --fix
    uv run ruff format .
    uv run codespell
# Run all pre-commit hooks
prek:
    uv run prek
# Install tools and git hooks, then sync dependencies
setup:
    brew bundle install
    uv run prek install
    just sync
# Sync all dependency groups
sync:
    uv sync --all-groups
# Run unit tests
test:
    uv run pytest
# Audit GitHub Actions workflows
zizmor:
    zizmor . --collect all
