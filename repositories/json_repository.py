import json
from pathlib import Path
from typing import Generic, TypeVar, Callable

from repositories.generic_repository import GenericRepository


T = TypeVar("T")


class JsonRepository(GenericRepository[T], Generic[T]):

    def __init__(
        self,
        filename: str,
        serializer: Callable[[T], dict],
        deserializer: Callable[[dict], T]
    ):
        super().__init__()

        self.filepath = Path(filename)

        # ADD THIS HERE
        self.filepath.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self.serializer = serializer
        self.deserializer = deserializer

        self.load()

    def save(self):

        data = [
            self.serializer(item)
            for item in self.items
        ]

        with self.filepath.open(
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

    def load(self):

        if not self.filepath.exists():
            return

        try:

            with self.filepath.open(
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

            self.items = [
                self.deserializer(item)
                for item in data
            ]

        except json.JSONDecodeError:

            print(
                f"Warning: Could not read {self.filepath}."
            )

            self.items = []

    def add(self, item: T):

        super().add(item)

        self.save()