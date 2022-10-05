# Skill

A place to create skill issues. Literally.

## How to use

This tutorial assumes that you have `poetry` installed.

```sh
make setup
```

### Create an issue

```sh
poetry run create-issue
```

This will prompt to enter the issue title and body, then a multi-selection picker will appear to choose the labels.
Afterwards, you will have to enter your GitHub credentials in order to publish the issue.

You can also pass the title and the body in the command:

```sh
poetry run create-issue --title Title --body "Body of my issue"
```

## Shortcuts

### Token

If you don't want to manually type your token every time, you can run:

```sh
make dotenv
```

Then, replace the placeholder in `.env` by your personal access token.

### Run

```sh
make create-issue
```

This installs the dependencies and runs the program.
