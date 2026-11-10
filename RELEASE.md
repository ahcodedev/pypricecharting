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
  `pyproject.toml`/`uv.lock`, builds the package, tags and publishes the GitHub Release with the
  build attached, then publishes the same build to [PyPI](https://pypi.org/project/pypricecharting/).
  The GitHub Release notes are the changelog
* The workflow regenerates the draft's notes when it starts, so edit the notes after the release
  is published, not before
* The version bump is committed as `Release vX.Y.Z` and pushed straight to `main`, with no PR.
  The tag points at that commit
* The first release must resolve to a version above the `0.0.1` in `pyproject.toml`, or the
  commit step fails with nothing to commit

## Release setup

The Release workflow depends on these settings outside the repository files:

* **Deploy key**: the release commit is pushed over SSH with a write-access deploy key. Its
  private half is the `RELEASE_DEPLOY_KEY` Actions secret. If `main` has a ruleset that requires
  pull requests or status checks, **Deploy keys** must be on its bypass list
* **PyPI trusted publisher**: PyPI trusts owner `ahcodedev`, repository `pypricecharting`,
  workflow `release.yml`, and environment `pypi`. No PyPI token is stored. Renaming the workflow
  file or the environment breaks publishing until PyPI is updated
* **`pypi` environment**: the `publish-pypi` job runs in the `pypi` GitHub environment. If it has
  required reviewers, the PyPI upload waits for approval after the GitHub Release is published
