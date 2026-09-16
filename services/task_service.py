from datetime import date, datetime, timedelta


class TaskService:
    """Provides task-related views that are independent of user input."""

    def get_due_tasks(self, tasks, today=None):
        """Group incomplete tasks that are overdue, due today, or due soon."""
        today = today or date.today()
        upcoming_limit = today + timedelta(days=7)

        due_tasks = {
            "overdue": [],
            "today": [],
            "upcoming": [],
        }

        for task in tasks:
            if task.completed:
                continue

            due_date = datetime.strptime(
                task.due_date,
                "%d-%m-%Y",
            ).date()

            if due_date < today:
                due_tasks["overdue"].append(task)
            elif due_date == today:
                due_tasks["today"].append(task)
            elif due_date <= upcoming_limit:
                due_tasks["upcoming"].append(task)

        for task_group in due_tasks.values():
            task_group.sort(
                key=lambda task: datetime.strptime(
                    task.due_date,
                    "%d-%m-%Y",
                ).date()
            )

        return due_tasks
