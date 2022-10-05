setup:
	poetry shell
	poetry update
	poetry install

create-issue: setup
	poetry run create-issue

dotenv:
	cp templates/.env .env
