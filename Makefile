all: setup

setup:
	poetry shell
	poetry update
	poetry install

dotenv:
	cp templates/.env .env

.PHONY: all setup dotenv
