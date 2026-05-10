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

#### Requirements.txt

```
No requirements.
```

#### Requirements.dev.txt

```
pre-commit==4.3.0
pip-audit==2.7.3
ruff==0.11.12
```

#### Requirements.test.txt

```
pytest==8.4.2
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
5. Execute: `pip install -r requirements.txt`
6. Execute: `pip install -r requirements.dev.txt`
7. Execute: `pip install -r requirements.test.txt`
8. Install the package in editable mode: `pip install -e .`
9. Run the project:
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
5. Execute: `pip install -r requirements.txt`
6. Execute: `pip install -r requirements.test.txt`
7. Install the package in editable mode: `pip install -e .`
8. Execute: `pytest --log-cli-level=INFO`

## Security Audit

You can check your dependencies for known vulnerabilities using **pip-audit**.

1. Go to the repository folder
2. Activate your virtual environment
3. Execute: `pip install -r requirements.dev.txt`
4. Execute: `pip-audit -r requirements.txt`

## Known Issues

None at the moment.

## Portfolio Link

[`https://www.diegolibonati.com.ar/#/project/propel`](https://www.diegolibonati.com.ar/#/project/propel)
