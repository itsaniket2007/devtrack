class LearningEntry:
    def __init__(self, topic, description, hours, difficulty):
        self.topic = topic
        self.description = description
        self.hours = hours
        self.difficulty = difficulty

    def display(self):
        print("\n-----------------------------")
        print(f"Topic       : {self.topic}")
        print(f"Description : {self.description}")
        print(f"Hours       : {self.hours}")
        print(f"Difficulty  : {self.difficulty}")
        print("-----------------------------")