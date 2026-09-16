import unittest
from datetime import date

from models.task import Task
from services.task_service import TaskService


class TaskServiceTests(unittest.TestCase):

    def setUp(self):
        self.service = TaskService()
        self.today = date(2026, 9, 17)

    def test_groups_incomplete_tasks_by_deadline(self):
        overdue = Task("Fix bug", "High", "16-09-2026")
        today_task = Task("Write tests", "Medium", "17-09-2026")
        upcoming = Task("Plan sprint", "Low", "20-09-2026")
        later = Task("Review goals", "Low", "25-09-2026")
        completed = Task("Done task", "Low", "17-09-2026")
        completed.mark_completed()

        due_tasks = self.service.get_due_tasks(
            [later, upcoming, completed, today_task, overdue],
            today=self.today,
        )

        self.assertEqual(due_tasks["overdue"], [overdue])
        self.assertEqual(due_tasks["today"], [today_task])
        self.assertEqual(due_tasks["upcoming"], [upcoming])


if __name__ == "__main__":
    unittest.main()
