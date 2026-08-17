class Task:

    def __init__(self, title, priority, due_date):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self._completed = False

    @property
    def completed(self):
        return self._completed

    @completed.setter
    def completed(self, value):

        if not isinstance(value, bool):
            raise ValueError("Completed status must be True or False.")

        self._completed = value

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