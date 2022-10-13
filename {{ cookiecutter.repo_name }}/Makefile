install:
	pip install poetry
	poetry install
	git init
	poetry run pre-commit install

test:
	poetry run pytest

lint:
	poetry run pre-commit

lint-all:
	poetry run pre-commit run --all-files
