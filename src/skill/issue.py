#!/usr/bin/env python3

# pyright: reportUnusedCallResult=false

import json
from argparse import ArgumentParser
from dataclasses import dataclass, field

import requests
from pick import pick
from result import Err, Ok, Result

from skill.constants import (
    ACCESS_TOKEN,
    DAHLIA,
    GITHUB_USERNAME,
    ISSUE_FOOTER,
    PRIVACY_NOTICE,
    REPO_API_URL,
    issue_labels,
)
from skill.utils import clean_exit


@dataclass
class Issue:
    number: int
    title: str
    body: str | None = None
    labels: list[str] = field(default_factory=list)

    def __repr__(self) -> str:
        return f"Issue #{self.number} {self.title!r}"


def open_issue(
    title: str, body: str | None = None, labels: list[str] = []
) -> Result[Issue, str]:
    """
    Ask for GitHub credentials and use them to make a request to open an issue in the repository.

    Args:
        title (str): the title of the issue
        body (Optional[str], optional): the body of the issue. Defaults to None.

    Returns:
        tuple[int, str]: the request code and message.
    """

    session = requests.Session()

    # We ask for user's GitHub credentials so we can create an issue using them
    print(PRIVACY_NOTICE)
    username = GITHUB_USERNAME or input("Enter your GitHub username: ")
    token = ACCESS_TOKEN or input("Enter your GitHub Personal Access Token: ")

    session.auth = (username, token)

    issue = {
        "title": title,
        "body": body,
        "labels": labels,
    }

    req = session.post(REPO_API_URL, json.dumps(issue))

    match req.status_code:
        case 201:
            number = json.loads(req.content)["number"]
            return Ok(Issue(number, title, body, labels))
        case 410:
            return Err("Issues are disabled in this repository.")
        case _:
            return Err("Could not create the issue.")


def init() -> tuple[str | None, ...]:
    parser = ArgumentParser()
    parser.add_argument("--title", default=None)
    parser.add_argument("--body", default=None)

    args = parser.parse_args()

    return args.title, args.body


@clean_exit
def main() -> None:
    """
    Main program.
    """

    _title, _body = init()

    title: str = _title or DAHLIA.input("\n&5Issue title:\n")
    body: str = _body or DAHLIA.input("\n&5Issue body (optional):\n")
    body += ISSUE_FOOTER
    picked_labels: list[tuple[str, int]] = pick(issue_labels, "Choose the labels", multiselect=True)  # type: ignore

    labels: list[str] = [issue_labels[index] for _, index in picked_labels]
    result = open_issue(title, body, labels)

    if result.is_ok():
        issue = result.unwrap()
        DAHLIA.print(f"&2{issue} was created successfully.")
    else:
        DAHLIA.print(f"&4Error: {result.value}")


if __name__ == "__main__":
    main()
