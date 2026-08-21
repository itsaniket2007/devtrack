from dataclasses import dataclass
@dataclass
class LearningEntry:
    topic: str
    description: str
    hours: float
    difficulty: str

    def display(self):
        print("\n-----------------------------")
        print(f"Topic       : {self.topic}")
        print(f"Description : {self.description}")
        print(f"Hours       : {self.hours}")
        print(f"Difficulty  : {self.difficulty}")
        print("-----------------------------")