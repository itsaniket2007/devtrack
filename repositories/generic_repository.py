from typing import Generic, TypeVar, Callable
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

    def find(self, condition: Callable[[T], bool]) -> list[T]:

        results = []

        for item in self.items:

            if condition(item):
                results.append(item)

        return results