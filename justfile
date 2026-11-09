ci-lint:
    uv run ty check
    uv run ruff check .
    uv run ruff format --check .
    uv run codespell
docs:
    uv run zensical serve
docs-build:
    uv run zensical build --strict
git-leaks:
    gitleaks git --pre-commit --staged --redact
lint:
    uv run ty check
    uv run ruff check . --fix
    uv run ruff format .
    uv run codespell
prek:
    uv run prek
setup:
    brew bundle install
    uv run prek install
    just sync
sync:
    uv sync --all-groups
test:
    uv run pytest
zizmor:
    zizmor . --collect all
