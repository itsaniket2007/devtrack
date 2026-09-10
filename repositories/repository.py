from typing import Protocol, TypeVar


T = TypeVar("T")


class Repository(Protocol[T]):
    """Common interface implemented by DevTrack repositories."""

    def add(self, item: T) -> None:
        ...

    def get_all(self) -> list[T]:
        ...

    def get_by_index(self, index: int) -> T | None:
        ...

    def count(self) -> int:
        ...
