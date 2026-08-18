class TaskRepository:

    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def get_all(self):
        return self.tasks

    def get_by_index(self, index):

        if 0 <= index < len(self.tasks):
            return self.tasks[index]

        return None