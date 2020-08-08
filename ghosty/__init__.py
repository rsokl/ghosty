from .objects import Person
import numpy as np


def identity(x: Person) -> Person:
    return x


def add1(x: float, y: float) -> float:
    return float(np.nan_to_num(x + y))


def add2(x: float, y: float) -> float:
    return float(np.nan_to_num(x + y))
