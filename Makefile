.PHONY: tests

install:
	poetry install

tests:
	poetry run pytest . -s

run:
	poetry run python formais/main.py

