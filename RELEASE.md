# Releases

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
  `ci/`, `docs/`, `refactor/`) and from the files it changes: `.github/workflows/*` adds `ci`,
  `*.md` adds `documentation`, and `uv.lock` adds `dependencies`. You can add or change them by hand
* Merging to `main` updates a draft GitHub Release with the next version and notes
* To release, run the **Release** workflow from the Actions tab. It bumps the version in
  `pyproject.toml`/`uv.lock`, tags the release, and uploads build artifacts. The GitHub Release
  notes are the changelog
* The Release workflow commits the version bump as `Release vX.Y.Z` and pushes it straight to
  `main` as `github-actions[bot]`, with no PR. The tag points at that commit. Branch protection
  on `main` must allow this push, or the workflow fails before the release is published
