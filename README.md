# Python Practice

## Set up
1. Clone repo
2. Make sure python3.12 is installed
3. [Install Poetry](https://python-poetry.org/docs/#installation)
4. Run `poetry install`
5. Run `poetry run pre-commit install`

## Tests
```sh
poetry run pytest
```

## Format
```sh
poetry run black src tests
```

## Lint
```sh
poetry run ruff src tests
```
