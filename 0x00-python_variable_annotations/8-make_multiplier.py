#!/usr/bin/env python3
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float, float]:
        def inner(multiplier: float) -> float:
            return (multiplier * multiplier)
        return inner
