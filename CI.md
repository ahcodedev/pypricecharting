# CI and Security

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
