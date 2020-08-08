__all__ = ["as_int", "as_Person", "Person"]


class Person:
    def __init__(self, x: int):
        self.x: int = x

    def __eq__(self, other: "Person"):
        return self.x == other.x


def as_int(x: Person) -> int:
    return x.x


def as_Person(x: int) -> Person:
    return Person(x)
