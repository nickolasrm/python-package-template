install:
	pip install poetry
	poetry install

test:
	poetry run pytest

lint:
	poetry run pre-commit

lint-all:
	poetry run pre-commit run --all-files
