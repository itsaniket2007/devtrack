class Task:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def display(self):
        status = "Completed" if self.completed else "Pending"

        print("\n-----------------------------")
        print(f"Task     : {self.title}")
        print(f"Priority : {self.priority}")
        print(f"Status   : {status}")
        print("-----------------------------")