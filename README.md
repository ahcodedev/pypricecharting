# PyPricecharting API Client ![](https://github.com/ahcode0919/pypricecharting/actions/workflows/python.yml/badge.svg?branch=main)
[![gitleaks](https://img.shields.io/badge/protected%20by-gitleaks-blue)](https://github.com/gitleaks/gitleaks)

Pricecharting API Client written in Python

## Setup

Project supports local development and VSCode Dev container development

### Local Development Installation

Note: Project uses `uv` and `just` to manage project configuration and commands

* Install `just` - `brew install just`
* Set up project - `just setup`
  * Installs Homebrew dependencies (`gitleaks`, `just`, `uv`)
  * Installs `prek` git hooks
  * Syncs project dependencies

### VS Code Dev Container

* Install Docker
* Install VSCode
* Open project folder in VS Code
* Optional - Install recommended extensions
* Reopen in container using Remote Development Container menu

## Project Commands

* `just setup` - install tools and git hooks, then sync dependencies
* `just sync` - sync project dependencies
* `just lint` - type check (`ty`), lint and format (`ruff`), and spellcheck (`codespell`). Fixes files in place
* `just ci-lint` - same checks as `just lint`, without modifying files
* `just test` - run unit tests
* `just prek` - run all pre-commit hooks
* `just git-leaks` - scan staged changes for secrets
* `uv add {package}` - install a dependency

### Pre-commit Hooks

`prek` runs these hooks on commit (configured in `prek.toml`):

* Built-in checks: trailing whitespace, end of file, large files, YAML, and JSON
* `just ci-lint`
* `just test`
* `gitleaks` secret scan of staged changes

## Usage

* Usage Notes

## Supporting Files

Project contains an OpenAPI spec and a Bruno project for easy testing and mocking

* `./bruno` - Bruno project
* `./open_api` - OpenApi spec
