#!/usr/bin/env python3

import functools
import json
import sys
import requests
from collections.abc import Callable
from typing import ParamSpec, TypeVar

from skill.constants import ISSUE_FOOTER, REPO_API_URL

P = ParamSpec("P")
R = TypeVar("R")


def clean_exit(func: Callable[P, R]) -> Callable[P, R]:
    """
    Clean the exit of a function in case of ^C by printing
    a simple message rather than a full error traceback.

    Args:
        func (Callable[P, R]): the function to wrap.

    Returns:
        Callable[P, R]: the wrapped function.
    """

    @functools.wraps(func)
    def inner(*args: P.args, **kwargs: P.kwargs) -> R:
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            print("\n\x1b[31mAborted. Exiting...\x1b[39m")
            raise SystemExit(0)

    return inner


def open_issue(title: str, body: str | None = None) -> tuple[int, str]:
    """
    Ask for GitHub credentials and use them to open an issue in the repository.

    Args:
        title (str): the title of the issue
        body (Optional[str], optional): the body of the issue. Defaults to None.

    Returns:
        tuple[int, str]: the request code and message.
    """

    session = requests.Session()

    # We ask for user's GitHub credentials so we can create an issue using them
    print(
        "\x1b[1;34mNote: no data is saved from the prompts. It is only used to make a request to GitHub.\x1b[0m\n"
    )
    username = input("Enter your GitHub username: ")
    token = input("Enter your GitHub Personal Access Token: ")

    session.auth = (username, token)

    issue = {
        "title": title,
        "body": body,
    }

    req = session.post(REPO_API_URL, json.dumps(issue))

    return req.status_code, req.content.decode("utf-8")


def debug_mode() -> bool:
    """
    Return whether the debug mode is on or off.
    """

    return "--debug" in sys.argv[1:]


@clean_exit
def main() -> None:
    """
    Main program.
    """

    title: str = input("\n\x1b[35mIssue title:\x1b[39m\n")
    body: str = input(
        "\n\x1b[35mType the issue body (optional):\x1b[39m\n"
    ) + ISSUE_FOOTER

    code, msg = open_issue(title, body)

    print()

    if str(code).startswith("2"):
        print(f"\x1b[32mIssue {title!r} was created successfully.")
    else:
        print("\x1b[31mError: Could not create the issue.\x1b[39m")
        if not debug_mode():
            print("Tip: use the flag --debug to print the detailed response.")

    if debug_mode():
        print(f"\nDetailed response:\n\t{msg}")


if __name__ == "__main__":
    main()
