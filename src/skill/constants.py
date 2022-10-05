"""
Skill constants.
"""

# pyright: reportUnusedCallResult=false, reportUnknownVariableType=false

import os

from dahlia import Dahlia, Depth
from dotenv import load_dotenv

load_dotenv()

DAHLIA = Dahlia(depth=Depth.LOW)

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", default=None)
GITHUB_USERNAME = os.environ.get("GITHUB_USERNAME", default=None)
REPO_API_URL = "https://api.github.com/repos/qexat/skill/issues"
ISSUE_FOOTER = "\n\n---\n<sup>Issue created with Skill issue CLI</sup>\n"

PRIVACY_NOTICE = DAHLIA.convert(
    "\n&9&lNote: no data is saved from the prompts. "
    "It is only used to make a request to GitHub.\n"
)

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
