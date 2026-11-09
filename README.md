# PyPriceCharting API Client ![](https://github.com/ahcodedev/pypricecharting/actions/workflows/python.yml/badge.svg?branch=main)
[![Security](https://github.com/ahcodedev/pypricecharting/actions/workflows/security.yml/badge.svg?branch=main)](https://github.com/ahcodedev/pypricecharting/actions/workflows/security.yml)
[![gitleaks](https://img.shields.io/badge/protected%20by-gitleaks-blue)](https://github.com/gitleaks/gitleaks)

PriceCharting API Client written in Python

## Setup

Project supports local development and VSCode Dev container development

### Local Development Installation

Note: Project uses `uv` (0.13.x, enforced by `required-version` in `pyproject.toml`) and `just` to
manage project configuration and commands

* Install `just` - `brew install just`
* Set up project - `just setup`
  * Installs Homebrew dependencies (`gitleaks`, `just`, `uv`, `zizmor`)
  * Installs `prek` git hooks
  * Syncs project dependencies

### VS Code Dev Container

* Install Docker
* Install VSCode
* Open project folder in VS Code
* Reopen in container using Remote Development Container menu

## Project Commands

* `just setup` - install tools and git hooks, then sync dependencies
* `just sync` - sync project dependencies
* `just lint` - type check (`ty`), lint and format (`ruff`), and spellcheck (`codespell`). Fixes files in place
* `just ci-lint` - same checks as `just lint`, without modifying files
* `just test` - run unit tests
* `just prek` - run all pre-commit hooks
* `just git-leaks` - scan staged changes for secrets
* `just zizmor` - audit GitHub Actions workflows for security issues
* `just docs` - serve the docs site locally with live reload
* `just docs-build` - build the docs site into `site/` in strict mode
* `uv add {package}` - install a dependency

### Pre-commit Hooks

`prek` runs these hooks on commit (configured in `prek.toml`):

* Built-in checks: trailing whitespace, end of file, large files, YAML, and JSON
* `just ci-lint`
* `just test`
* `gitleaks` secret scan of staged changes

## CI and Security

See [CI.md](CI.md) for the GitHub Actions workflows and Dependabot setup.

## Documentation

The docs site is built with [Zensical](https://zensical.org) from `mkdocs.yml` and the pages in
`docs/`. API reference pages are generated from docstrings with `mkdocstrings`. The `docs.yml`
workflow deploys the site to GitHub Pages on every push to `main`.

## Releases

See [RELEASE.md](RELEASE.md) for how releases and release labels work.

## Usage

The client is under development. `PriceCharting` and `AsyncPriceCharting` can be created and used
as context managers, but their API methods are not implemented yet.

```python
from pypricecharting import AsyncPriceCharting, PriceCharting

with PriceCharting("<40-character API token>") as client:
    ...

async with AsyncPriceCharting("<40-character API token>") as client:
    ...
```

## Supporting Files

Project contains an OpenAPI spec and a Bruno project for easy testing and mocking

* `./bruno` - Bruno project
* `./open_api` - OpenAPI spec
