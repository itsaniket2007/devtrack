from typing import Generic, TypeVar


T = TypeVar("T")


class GenericRepository(Generic[T]):

    def __init__(self):
        self.items: list[T] = []

    def add(self, item: T):
        self.items.append(item)

    def get_all(self) -> list[T]:
        return self.items

    def get_by_index(self, index: int) -> T | None:

        if 0 <= index < len(self.items):
            return self.items[index]

        return None

    def count(self) -> int:
        return len(self.items)