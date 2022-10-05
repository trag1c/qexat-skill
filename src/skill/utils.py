#!/usr/bin/env python3

import functools
from collections.abc import Callable
from typing import ParamSpec, TypeVar

from skill.constants import DAHLIA

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
            DAHLIA.print("\n&4Aborted. Exiting...")
            raise SystemExit(0)

    return inner
