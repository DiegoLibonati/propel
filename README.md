# TaskManager-Library-Python

## Educational Purpose

This project was created primarily for **educational and learning purposes**.
While it is well-structured and could technically be used in production, it is **not intended for commercialization**.
The main goal is to explore and demonstrate best practices, patterns, and technologies in software development.

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
    1. From CLI: `python -m task_manager.manager`
    2. Or import as a library in Python: `from task_manager import Manager, Task`

### Pre-Commit for Development

1. Once you're inside the virtual environment, let's install the hooks specified in the pre-commit. Execute: `pre-commit install`
2. Now every time you try to commit, the pre-commit lint will run. If you want to do it manually, you can run the command: `pre-commit run --all-files`

## Description

Task manager developed in Python that allows you to manage personal or team activities. With this tool, users can create, edit and organize their tasks, assigning due dates and setting priorities. Ideal for those who need a simple but functional solution to organize their tasks effectively.

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
```

#### Requirements.test.txt

```
pytest==8.4.2
pytest-env==1.1.5
pytest-cov==4.1.0
pytest-timeout==2.3.1
pytest-xdist==3.5.0
```

## Portfolio Link

[`https://www.diegolibonati.com.ar/#/project/TaskManager-Library-Python`](https://www.diegolibonati.com.ar/#/project/TaskManager-Library-Python)

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