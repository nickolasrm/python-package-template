# {{ cookiecutter.python_package }}
{{ cookiecutter.description }}

## Usage

The documentation is hosted on [Read the Docs](https://readthedocs.org/). You can find the latest version of the documentation [here](https://{{ cookiecutter.repo_name }}.readthedocs.io/en/latest/).

## Development

To contribute to this repository, please follow the steps below:

1. Make sure you have `make` installed on your system.
2. Run `make install` to install `poetry`, `pre-commit`, and dev dependencies.
3. Make your changes.
4. Write unit tests under `tests/` and run `make test` to run them.
5. Run `make lint` to lint your code.
6. Open a pull request.

## Authors

{% set authors = cookiecutter.author.split(',') -%}
{% set emails = cookiecutter.email.split(',') -%}
{% for author in authors -%}
- {{ authors[loop.index0].strip() }} [{{ emails[loop.index0].strip() }}](mailto:{{ emails[loop.index0].strip() }})
{% endfor -%}
