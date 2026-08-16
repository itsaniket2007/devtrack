from datetime import datetime


class Task:

    def __init__(self, title, priority, due_date):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def display(self):

        status = "Completed" if self.completed else "Pending"

        print("\n-----------------------------")
        print(f"Task      : {self.title}")
        print(f"Priority  : {self.priority}")
        print(f"Due Date  : {self.due_date}")
        print(f"Status    : {status}")
        print("-----------------------------")