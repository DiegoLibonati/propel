# Propel

## Educational Purpose

This project was created primarily for **educational and learning purposes**.
While it is well-structured and could technically be used in production, it is **not intended for commercialization**.
The main goal is to explore and demonstrate best practices, patterns, and technologies in software development.

## Description

**Propel** is a Python library for managing tasks through a well-defined lifecycle. It provides two core building blocks: `TaskModel`, which represents a single unit of work, and `Manager`, which acts as the central controller that holds and orchestrates all tasks.

Each task carries a title, a description, an expiration date, and a state. States follow a fixed vocabulary — `pending`, `in_progress`, and `complete` — so the lifecycle of every task is always explicit and predictable. A task starts as `pending` by default and can be transitioned to any valid state at any point using `change_state()`. Fields like title, description, and expiration date can be updated after creation through the `edit()` method, which requires at least one field to be provided, preventing accidental no-op updates.

The `Manager` stores tasks internally in a dictionary keyed by their UUID, which makes lookups fast regardless of the number of tasks. It exposes methods to add a task (`add_task`), remove it by ID (`remove_task`), edit its fields (`edit_task`), move it to a different state (`move_task_by_state`), and log the full list of current tasks to the console (`logging_task`). Every operation validates its inputs before executing: passing an invalid type, an empty ID, a non-existent task, or a duplicate will raise a typed exception from the custom exception hierarchy — `ValidationError`, `NotFoundError`, or `ConflictError` — each carrying both a machine-readable code and a human-readable message.

The exception system is built on a shared `BaseError` base class, which means consumers can catch exceptions at any level of specificity — a specific subclass, or `BaseError` to handle all library errors in one place. Error codes and messages are defined as named constants in dedicated modules, keeping them decoupled from the logic that raises them.

Logging is handled by a factory function, `setup_logger`, that creates named loggers with a consistent format and deduplicates handlers automatically, so importing the library in different parts of a codebase never produces repeated log lines.

The package follows the `src` layout, ships with a complete test suite using `pytest`, and enforces code style through `ruff` and `pre-commit` hooks.

## Technologies used

1. Python >= 3.11

## Libraries used

Dependencies are declared in `pyproject.toml` and split into optional groups so production installs stay minimal.

#### Runtime (`[project.dependencies]`)

```
# no third-party runtime dependencies
```

#### Dev (`[project.optional-dependencies]` dev)

```
pre-commit==4.3.0
pip-audit==2.7.3
ruff==0.11.12
mypy==1.13.0
```

#### Test (`[project.optional-dependencies]` test)

```
pytest==9.0.3
pytest-env==1.1.5
pytest-cov==4.1.0
pytest-timeout==2.3.1
pytest-xdist==3.5.0
```

## Getting Started

1. Clone the repository
2. Go to the repository folder and execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Install the package in editable mode with development and test extras: `pip install -e .[dev,test]`
6. Run the project:
    1. From CLI: `python -m propel.manager`
    2. Or import as a library in Python: `from propel import Manager, TaskModel`

### Pre-Commit for Development

1. Once you're inside the virtual environment, let's install the hooks specified in the pre-commit. Execute: `pre-commit install`
2. Now every time you try to commit, the pre-commit lint will run. If you want to do it manually, you can run the command: `pre-commit run --all-files`

## Testing

1. Go to the repository folder
2. Execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Install the package in editable mode with the test extras: `pip install -e .[test]`
6. Execute: `pytest --log-cli-level=INFO`

## Security Audit

You can check your dependencies for known vulnerabilities using **pip-audit**.

1. Go to the repository folder
2. Activate your virtual environment
3. Install the dev extras: `pip install -e .[dev]`
4. Execute: `pip-audit`

## Continuous Integration

The repository ships with a **GitHub Actions** pipeline defined in [`.github/workflows/ci.yml`](.github/workflows/ci.yml). It runs automatically on every `push` and `pull_request` targeting the `main` branch. On `push` to `main`, the same workflow continues with a final job that produces an automated release.

### Pipeline overview

```
                      ┌─── PR or push to main ───┐
                      ▼                          ▼
┌──────────────────────┐  ┌──────────────────────┐  ┌──────────────────────┐
│   lint-and-audit     │─▶│       testing        │─▶│        build         │
│ ruff · mypy · audit  │  │ pytest · 3.11/12/13  │  │ python -m build sdist│
└──────────────────────┘  └──────────────────────┘  └──────────────────────┘
                                                          │
                                          (only on push to main)
                                                          ▼
                                                ┌──────────────────────┐
                                                │       release        │
                                                │ python-semantic-release│
                                                └──────────────────────┘
```

### Validation jobs (run on every PR and push)

1. **`lint-and-audit`** — `ruff check .`, `ruff format --check .`, `mypy --config-file=pyproject.toml .`, and `pip-audit` for known dependency vulnerabilities. Runs on Python 3.13.
2. **`testing`** — installs the `[test]` extras and runs `pytest --cov=src --cov-report=term` across a matrix of Python `3.11`, `3.12` and `3.13` (with `fail-fast: false`, so one failing version does not cancel the others).
3. **`build`** — runs `python -m build` and verifies that a source distribution (`dist/*.tar.gz`) is produced, smoke-testing that the package is shippable.

### Release job (only on push to `main`)

4. **`release`** — runs [`python-semantic-release`](https://python-semantic-release.readthedocs.io/), which inspects the commits since the latest tag, decides the next SemVer version using [Conventional Commits](#conventional-commits-required-for-releases), updates `CHANGELOG.md` and the version in `pyproject.toml`, then commits (with the message `chore(release): v{version} [skip release]`), tags as `v{version}` and pushes back to `main`, finally creating the matching GitHub Release with the built `*.whl` and `*.tar.gz` attached. The release commit's `[skip release]` marker prevents the workflow from triggering itself in a loop.

### Conventional Commits (required for releases)

Commits merged into `main` must follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) so the pipeline can compute the next version and group the changelog entries.

| Commit prefix | Version bump | Example |
|---|---|---|
| `feat:` / `feat(scope):` | **MINOR** | `feat(manager): add bulk remove_tasks` |
| `fix:` / `fix(scope):` | **PATCH** | `fix: prevent crash on empty task id` |
| `perf:` / `perf(scope):` | **PATCH** | `perf: speed up state lookup` |
| `refactor:`, `docs:`, `build:`, `ci:`, `chore:`, `style:`, `test:` | **no release** | `refactor: extract state validator` |
| `feat!:` / `fix!:` or `BREAKING CHANGE:` in the body | **MAJOR** *(see note)* | `feat!: rename TaskModel to Task` |

Only `feat:`, `fix:` and `perf:` trigger a release. The other allowed prefixes (`refactor`, `docs`, `build`, `ci`, `chore`, `style`, `test`) are recognized by the changelog grouping but do **not** bump the version on their own — push one of those alone and the `release` job will run but produce no new release.

> **Note on MAJOR bumps while at `0.x.y`**: `major_on_zero` is disabled. While the project version is still in the `0.x.y` range, a breaking change (`feat!:` / `BREAKING CHANGE:`) bumps the **minor** segment instead of moving to `1.0.0`. Major bumps only kick in once the version reaches `1.0.0` or higher.

When a push contains multiple commits, the highest applicable bump wins (a single `feat:` among many `fix:` triggers a MINOR bump). If you squash-merge PRs, configure the repo to use the PR title as the squash commit message and write the **PR title** following the convention.

### Skipping a release

If you need to push a change to `main` without producing a release (e.g. tweaking job names in the workflow, fixing a typo in the README), append `[skip release]` to the commit message. The validation jobs (`lint-and-audit`, `testing`, `build`) still run; only the `release` job is skipped.

```bash
git commit -m "ci: rename build job for clarity [skip release]"
```

To skip **everything** including validation, use GitHub's standard `[skip ci]` marker instead.

### Where the build outputs live

| Output | Location |
|---|---|
| Validation logs (lint, mypy, audit, tests) | **Actions** tab on GitHub |
| Source distribution (`*.tar.gz`) and wheel (`*.whl`) | Attached as assets to the corresponding **GitHub Release** |
| Version history & notes | [`CHANGELOG.md`](CHANGELOG.md) + Releases page |
| Tagged versions (`v{version}`) | **Releases** page (sidebar of the repo) |

> **Note:** GitHub's **Packages** section is for package registries (npm, PyPI, Docker, etc.) and does not host source tarballs. Tagged versions and their changelog entries always live under **Releases**.

### Repository setup required for releases

For the `release` job to push tags and commits back to `main`, the repository needs:

1. **Settings → Actions → General → Workflow permissions**: set to *Read and write permissions*.
2. **Branch protection on `main`**: if enabled, allow the `github-actions[bot]` to bypass the PR requirement, or disable the protection for the bot. Otherwise `release` will fail when pushing the version bump.

### Running the same checks locally

```bash
# lint-and-audit
ruff check .
ruff format --check .
mypy --config-file=pyproject.toml .
pip-audit

# testing
pytest --cov=src --cov-report=term

# build
python -m build
```

## Known Issues

None at the moment.

## Portfolio Link

[`https://www.diegolibonati.com.ar/#/project/propel`](https://www.diegolibonati.com.ar/#/project/propel)
