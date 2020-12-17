# surferrr

Control web browser like a surfer.

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
