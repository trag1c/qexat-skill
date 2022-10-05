"""
Skill constants.
"""

import dotenv
import os

dotenv.load_dotenv()  # type: ignore

ACCESS_TOKEN = os.environ["ACCESS_TOKEN"] or None
GITHUB_USERNAME = os.environ["GITHUB_USERNAME"] or None
REPO_API_URL = "https://api.github.com/repos/qexat/skill/issues"
ISSUE_FOOTER = "\n\n---\n<sup>Issue created with Skill issue CLI</sup>\n"

PRIVACY_NOTICE = "\n\x1b[1;34mNote: no data is saved from the prompts. It is only used to make a request to GitHub.\x1b[0m\n"

issue_labels: list[str] = [
    "bug",
    "documentation",
    "duplicate",
    "enhancement",
    "good first issue",
    "help wanted",
    "invalid",
    "question",
    "test",
    "wontfix",
]
