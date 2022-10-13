authors = "{{ cookiecutter.author }}".split(",")
emails = "{{ cookiecutter.email }}".split(",")

assert len(authors) == len(emails), "Number of authors and emails must be equal"
