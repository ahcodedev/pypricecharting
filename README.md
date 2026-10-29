# Python Project Template ![](https://github.com/ahcode0919/python-project-template/actions/workflows/ci.yml/badge.svg?branch=main)

Baseline Python project template

## Setup

Project supports local development and VSCode Dev container development

### Local Development Installation

Note: Project uses `uv` and `just` to manage project configuration and commands

* Install dependencies via Homebrew - `brew bundle install`
* Sync project - `just sync`

### VS Code Dev Container

* Install Docker
* Install VSCode
* Open project folder in VS Code
* Install recommended extensions
* Reopen in container using Remote Development Container menu

## Project Commands

* Local
  * `just lint` - lint project files
* Dev container
  * `just lint` - lint and stylecheck project files
* Run unit tests: `just test`
* Install dependency: `uv add {package}`

## Usage

* Usage Notes
