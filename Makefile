.PHONY: all
all: setup

.PHONY: setup
setup:
	poetry shell
	poetry update
	poetry install

.PHONY: dotenv
dotenv:
	cp templates/.env .env
