# Python Package Template

Python package project template.

## Steps

1. Add development packages

   ```sh
   poetry add --dev yapf flake8 cohesion flake8-blind-except flake8-bugbear flake8-class-newline flake8-commas flake8-builtins flake8-coding flake8-docstrings flake8-import-order flake8-quotes flake8-comprehensions flake8-eradicate pep8-naming mypy pytest pytest-cov flake8-html
   ```

1. Rename folders.
   * `./src/pkg_name` to the package name.
   * `./tests/pkg_name` to the package name.
1. Edit `pyproject.toml`
   * Replace **<REPO_NAME>** to the repostory name.
   * **pkg-name** to the package name.
1. Integrate to CircleCI.

## Development

* Requirements: poetry, pyenv

```sh
# Setup
poetry install

# Lint & Test
poetry run flake8 --format=html --htmldir=report/flake-report .
poetry run pytest --cov-report html:report/coverage --cov=combu tests/

# Build and publish
poetry build
poetry publish
```
