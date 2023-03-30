#!/usr/bin/env python3
"""Annotation"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotation"""
    return [(i, len(i)) for i in lst]
