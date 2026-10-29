lint:
    uv run ruff check . --fix
    uv run ruff format .
    uv run codespell
sync:
    uv sync --all-groups
test:
    uv run pytest