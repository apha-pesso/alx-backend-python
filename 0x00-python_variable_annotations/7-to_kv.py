#!/usr/bin/env python3
"""Tuple from float and int"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return Tuple"""
    return (k, v * v)
