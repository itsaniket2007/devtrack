from dataclasses import dataclass


@dataclass
class LearningEntry:

    topic: str
    description: str
    hours: float
    difficulty: str

    def __post_init__(self):

        if not self.topic.strip():
            raise ValueError("Learning topic cannot be empty.")

        if not self.description.strip():
            raise ValueError("Learning description cannot be empty.")

        if self.hours <= 0:
            raise ValueError("Learning hours must be greater than 0.")

        allowed_difficulties = {
            "easy",
            "medium",
            "hard"
        }

        if self.difficulty.lower() not in allowed_difficulties:
            raise ValueError(
                "Difficulty must be Easy, Medium, or Hard."
            )

    def display(self):

        print("\n-----------------------------")
        print(f"Topic       : {self.topic}")
        print(f"Description : {self.description}")
        print(f"Hours       : {self.hours}")
        print(f"Difficulty  : {self.difficulty}")
        print("-----------------------------")