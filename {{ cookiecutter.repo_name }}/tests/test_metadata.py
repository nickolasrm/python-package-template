"""Tests if duplicated metadata matches across multiple parts of the code."""
import re
import {{ cookiecutter.python_package }}

import pytest
import tomli

import docs.source.conf as docs


@pytest.fixture(name="metadata")
def fixture_metadata() -> dict:
    """Returns metadata from pyproject.toml."""
    with open("pyproject.toml", "rb") as file:
        toml = tomli.load(file)
        return toml["tool"]["poetry"]


def test_version(metadata: dict):
    """Checks if version matches."""
    assert {{ cookiecutter.python_package }}.__version__ == metadata["version"]
    assert docs.release == metadata["version"]


def test_author(metadata: dict):
    """Checks if author names match pyproject.toml's."""
    plain_authors = ", ".join(metadata["authors"])
    plain_authors = re.sub(r"\s?<.+?>", "", plain_authors)  # remove emails
    assert docs.author == plain_authors
