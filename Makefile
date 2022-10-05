setup:
	poetry shell
	poetry update
	poetry install

create-issue: setup
	poetry run create-issue
