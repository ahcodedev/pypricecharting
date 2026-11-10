# CI and Security

| Workflow                                          | Runs on                      | Purpose                                        |
| ------------------------------------------------- | ---------------------------- | ---------------------------------------------- |
| `python.yml`                                      | push / PR to `main`          | lint and unit tests                            |
| `security.yml`                                    | push to `main`, all PRs      | zizmor workflow audit, gitleaks secret scan    |
| `release-drafter.yml`                             | push to `main`, PRs          | update the draft release, label PRs            |
| `release.yml`                                     | manual                       | publish a release to GitHub and PyPI           |
| `docs.yml`                                        | push / PR to `main`, manual  | build docs, deploy to GitHub Pages (not PRs)   |

* The docs site deploys through GitHub Pages, so the repo's Pages source must be set to
  **GitHub Actions**. PRs build the docs in strict mode without deploying
* On PRs, `release-drafter.yml` also runs the `require-label` check, which fails until the PR has
  at least one release label (see [RELEASE.md](RELEASE.md))
* `release.yml` has two jobs. `release` bumps the version, builds, pushes the release commit with
  a deploy key, and publishes the GitHub Release. `publish-pypi` then uploads the same build to
  PyPI with trusted publishing, from the `pypi` environment. See [RELEASE.md](RELEASE.md) for the
  settings it needs
* GitHub Actions are pinned to full commit SHAs, with the version in a trailing comment
* Dependabot (`.github/dependabot.yml`) checks weekly for updates to GitHub Actions and Python
  dependencies, and monthly for the dev container image and dev container features. New releases
  wait 7 days before an update is proposed. Dependabot PRs get the `dependencies` label
