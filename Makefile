.PHONY: tests

install:
	poetry install

tests:
	poetry run pytest . -s
