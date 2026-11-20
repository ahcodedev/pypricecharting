# PyPriceCharting API Client

[![CI](https://github.com/ahcodedev/pypricecharting/actions/workflows/python.yml/badge.svg?branch=main)](https://github.com/ahcodedev/pypricecharting/actions/workflows/python.yml)
[![Docs](https://github.com/ahcodedev/pypricecharting/actions/workflows/docs.yml/badge.svg?branch=main)](https://github.com/ahcodedev/pypricecharting/actions/workflows/docs.yml)
[![Security](https://github.com/ahcodedev/pypricecharting/actions/workflows/security.yml/badge.svg?branch=main)](https://github.com/ahcodedev/pypricecharting/actions/workflows/security.yml)
[![betterleaks](https://img.shields.io/badge/protected%20by-betterleaks-blue)](https://github.com/betterleaks/betterleaks)
[![zizmor](https://img.shields.io/badge/%F0%9F%8C%88-zizmor-white?labelColor=white)](https://zizmor.sh/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
![Python](https://img.shields.io/badge/python-3.15-blue)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](https://github.com/ahcodedev/pypricecharting/blob/main/LICENSE)

PriceCharting API Client written in Python

## Setup

Project supports local development and VSCode Dev container development

### Local Development Installation

Note: Project uses `uv` and `just` to manage project configuration and commands

* Install `just` - `brew install just`
* Set up project - `just setup`
  * Installs Homebrew dependencies from the `Brewfile`
  * Installs `prek` git hooks
  * Syncs project dependencies

### VS Code Dev Container

* Install Docker
* Install VSCode
* Open project folder in VS Code
* Reopen in container using Remote Development Container menu

## Project Commands

* `just setup` - install Homebrew tools from the `Brewfile` and sync the project
* `just sync` - sync project dependencies (all groups)
* `just lint` - type check, lint, format, spell check (typos), and lint workflows (actionlint), YAML (yamllint),
  and JSON (jq) (applies fixes)
* `just ci-lint` - run the same checks without modifying files, except spell check (used in CI)
* `just spellcheck` - check spelling with typos
* `just test` - run unit tests
* `just coverage` - run unit tests with coverage (fails under 98%)
* `just build` - build the sdist and wheel into `dist/`
* `just audit` - check dependencies for known vulnerabilities with pip-audit
* `just markdownlint` - lint Markdown files with markdownlint-cli2
* `just docs-build` - build the docs site with Zensical (strict mode, output in `site/`)
* `just docs-serve` - serve the docs locally with live reload
* `just prek` - run pre-commit hooks via prek
* `just betterleaks` - scan staged changes for secrets with betterleaks
* `just zizmor` - audit GitHub Actions workflows for security issues
* `just set-github-labels` - remove GitHub's non-release default labels, then create or update the release labels
  (for fresh repos, requires `gh auth login`)
* `just update-template` - pull in the latest changes from the Copier template
* `uv add {package}` - install a dependency

### Pre-commit Hooks

`prek` runs these hooks on commit (configured in `prek.toml`):

* Built-in checks: trailing whitespace, end of file, large files, YAML, and JSON
* `just ci-lint`
* `just test`
* `just docs-build` (when `docs/`, `src/`, or `mkdocs.yml` change)
* `just markdownlint` (when Markdown files change)
* `just audit` (when `pyproject.toml` or `uv.lock` change)
* `betterleaks` secret scan of staged changes

## CI

See [CI.md](https://github.com/ahcodedev/pypricecharting/blob/main/CI.md) for the GitHub Actions workflows and
Dependabot setup.

## Documentation

The docs site is built with [Zensical](https://zensical.org) from `mkdocs.yml` and the pages in
`docs/`. API reference pages are generated from docstrings with `mkdocstrings`. The `docs.yml`
workflow deploys the site to GitHub Pages on every push to `main`.

## Releases

Releases are published to GitHub Releases and to [PyPI](https://pypi.org/project/pypricecharting/)
by the `Release` workflow. See
[RELEASE.md](https://github.com/ahcodedev/pypricecharting/blob/main/RELEASE.md) for how releases
and release labels work.

## Usage

Both clients have a method for every Prices API and Marketplace API operation.

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

## TODO / Investigate

* **Offer details price limits** - `OfferDetailsResponse` reads `price-max` and `price-min`, the
  names in the documentation's key table. If the API sends `max-price` and `min-price` instead,
  `price_max` and `price_min` come back as `None` with no error. Validate `/api/offer-details`
* **Extra Marketplace keys** - `pending-reason`, `seller-id`, `image-url`, `best-competing-price`,
  `is-best-priced-offer` and `value` are only on `OfferDetailsResponse`. The documentation doesn't
  say which endpoint returns each one. If `/api/offers` returns any of them, add them to `Offer`
