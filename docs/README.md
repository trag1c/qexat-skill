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

### GitHub credentials

If you don't want to manually type your GitHub credentials every time, you can run:

```sh
make dotenv
```

Then, replace the placeholders in `.env` by your username and your personal access token.

## Contribute

I'm fully open to contributions! Please read [CONTRIBUTING.md](/docs/CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](/docs/CODE_OF_CONDUCT.md) before opening a pull request.

## Roadmap

The roadmap of the project can be found [here](https://github.com/users/qexat/projects/1).
