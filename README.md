# PyPriceCharting API Client

[![CI](https://github.com/ahcodedev/pypricecharting/actions/workflows/python.yml/badge.svg?branch=main)](https://github.com/ahcodedev/pypricecharting/actions/workflows/python.yml)
[![Docs](https://github.com/ahcodedev/pypricecharting/actions/workflows/docs.yml/badge.svg?branch=main)](https://github.com/ahcodedev/pypricecharting/actions/workflows/docs.yml)
[![Security](https://github.com/ahcodedev/pypricecharting/actions/workflows/security.yml/badge.svg?branch=main)](https://github.com/ahcodedev/pypricecharting/actions/workflows/security.yml)
[![gitleaks](https://img.shields.io/badge/protected%20by-gitleaks-blue)](https://github.com/gitleaks/gitleaks)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
![Python](https://img.shields.io/badge/python-3.15-blue)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

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

Under development: the Prices API methods (`product`, `products`) and the Marketplace `offers`
method are implemented; the other Marketplace API methods are not yet.

```python
from pypricecharting import AsyncPriceCharting, PriceCharting

with PriceCharting("<40-character API token>") as client:
    game = client.product(id="6910")
    print(game.product_name, game.cib_price)  # prices are in pennies

async with AsyncPriceCharting("<40-character API token>") as client:
    game = await client.product(q="earthbound")
    results = await client.products("chrono trigger")  # up to 20 matches
```

Without a token argument, the token is read from `PRICECHARTING_TOKEN`. See the docs site for
errors and client options.

## Supporting Files

Project contains an OpenAPI spec and a Bruno project for easy testing and mocking

* `./bruno` - Bruno project
* `./open_api` - OpenAPI spec
