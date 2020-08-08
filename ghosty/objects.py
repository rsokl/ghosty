class Person:
    def __init__(self, x: int):
        self.x = x

    def __eq__(self, other: "Person"):
        return self.x == other.x