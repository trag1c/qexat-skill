#!/usr/bin/env python3

import json
import requests

from pick import pick

from skill.constants import ISSUE_FOOTER, REPO_API_URL, issue_labels
from skill.utils import clean_exit, debug_mode


def open_issue(
    title: str, body: str | None = None, labels: list[str] = []
) -> tuple[int, str]:
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
        "\n\x1b[1;34mNote: no data is saved from the prompts. It is only used to make a request to GitHub.\x1b[0m\n"
    )
    username = input("Enter your GitHub username: ")
    token = input("Enter your GitHub Personal Access Token: ")

    session.auth = (username, token)

    issue = {
        "title": title,
        "body": body,
        "labels": labels,
    }

    req = session.post(REPO_API_URL, json.dumps(issue))

    return req.status_code, req.content.decode("utf-8")


@clean_exit
def main() -> None:
    """
    Main program.
    """

    title: str = input("\n\x1b[35mIssue title:\x1b[39m\n")
    body: str = (
        input("\n\x1b[35mIssue body (optional):\x1b[39m\n") + ISSUE_FOOTER
    )
    picked_labels: list[tuple[str, int]] = pick(issue_labels, "Choose the labels", multiselect=True)  # type: ignore

    labels: list[str] = [issue_labels[index] for _, index in picked_labels]
    code, msg = open_issue(title, body, labels)

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
