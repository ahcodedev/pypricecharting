# PyPricecharting API Client ![](https://github.com/ahcode0919/pypricecharting/actions/workflows/python.yml/badge.svg?branch=main)
[![Security](https://github.com/ahcode0919/pypricecharting/actions/workflows/security.yml/badge.svg?branch=main)](https://github.com/ahcode0919/pypricecharting/actions/workflows/security.yml)
[![gitleaks](https://img.shields.io/badge/protected%20by-gitleaks-blue)](https://github.com/gitleaks/gitleaks)

Pricecharting API Client written in Python

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
* Optional - Install recommended extensions
* Reopen in container using Remote Development Container menu

The base image, `just`, and `uv` are pinned by version and digest in `.devcontainer/Dockerfile`
and updated by Dependabot. To change the Python version, edit the `FROM` line.

## Project Commands

* `just setup` - install tools and git hooks, then sync dependencies
* `just sync` - sync project dependencies
* `just lint` - type check (`ty`), lint and format (`ruff`), and spellcheck (`codespell`). Fixes files in place
* `just ci-lint` - same checks as `just lint`, without modifying files
* `just test` - run unit tests
* `just prek` - run all pre-commit hooks
* `just git-leaks` - scan staged changes for secrets
* `just zizmor` - audit GitHub Actions workflows for security issues
* `uv add {package}` - install a dependency

### Pre-commit Hooks

`prek` runs these hooks on commit (configured in `prek.toml`):

* Built-in checks: trailing whitespace, end of file, large files, YAML, and JSON
* `just ci-lint`
* `just test`
* `gitleaks` secret scan of staged changes

## CI and Security

| Workflow                                          | Runs on                      | Purpose                                        |
| ------------------------------------------------- | ---------------------------- | ---------------------------------------------- |
| `python.yml`                                      | push / PR to `main`          | lint and unit tests                            |
| `security.yml`                                    | push to `main`, all PRs      | zizmor workflow audit, gitleaks secret scan    |
| `release-drafter.yml`                             | push to `main`, PRs          | update the draft release, label PRs            |
| `release.yml`                                     | manual                       | publish a release                              |

* GitHub Actions are pinned to full commit SHAs, with the version in a trailing comment
* Dependabot (`.github/dependabot.yml`) checks weekly for updates to GitHub Actions, Python
  dependencies, the dev container image, and dev container features. New releases wait 7 days
  before an update is proposed. Dependabot PRs get the `dependencies` label

## Releases

Releases are managed with [Release Drafter](https://github.com/release-drafter/release-drafter),
which reads the **release labels** on merged pull requests.

A release label is a GitHub label added to the pull request itself, from the **Labels** section
of the PR sidebar. Release Drafter only reads these labels. Commit messages and PR titles are not
parsed, so prefixes like `feat:` or `fix:` have no effect. Only the labels below count as release
labels; other repository labels (e.g. `good first issue`, `question`) are ignored.

| Release label                                                     | Version bump | Release notes section |
| ----------------------------------------------------------------- | ------------ | --------------------- |
| `breaking`                                                        | major        | Breaking Changes      |
| `feature`, `enhancement`                                          | minor        | Features              |
| `bug`, `fix`                                                      | patch        | Bug Fixes             |
| `chore`, `ci`, `dependencies`, `documentation`, `refactor`        | patch        | Maintenance           |
| `skip-changelog`                                                  | none         | Excluded              |

* Every PR must have at least one release label, or the `Release Drafter / require-label` check fails. If a release
  has PRs with different labels, the largest bump wins
* Release labels are added automatically from the PR's branch name prefix (`feat/`, `fix/`, `chore/`,
  `ci/`, `docs/`, `refactor/`) and from the files it changes. You can add or change them by hand
* Merging to `main` updates a draft GitHub Release with the next version and notes
* To release, run the **Release** workflow from the Actions tab. It bumps the version in
  `pyproject.toml`/`uv.lock`, updates `CHANGELOG.md`, tags the release, and uploads build artifacts

## Usage

* Usage Notes

## Supporting Files

Project contains an OpenAPI spec and a Bruno project for easy testing and mocking

* `./bruno` - Bruno project
* `./open_api` - OpenApi spec
