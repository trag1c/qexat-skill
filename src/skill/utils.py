#!/usr/bin/env python3

import functools
from collections.abc import Callable
from typing import ParamSpec, TypeVar

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
