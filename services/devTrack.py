from datetime import datetime
from models.learning import LearningEntry
from models.project import Project
from models.task import Task
from utils.valiadators import validate_email
from utils.status import ProjectStatus
from repositories.project_repository import ProjectRepository
from repositories.task_repository import TaskRepository
from utils.logger import logger
from utils.exceptions import TaskAlreadyCompletedError
from services.report_service import ReportService
from repositories.generic_repository import GenericRepository


class DevTrack:

    def __init__(self):

        self.learning_repository = GenericRepository[LearningEntry]()
        self.project_repository = GenericRepository[Project]()
        self.task_repository = GenericRepository[Task]()

        self.report_service = ReportService()

    # ==========================================
    # LEARNING
    # ==========================================

    def add_learning(self):

        print("\n===== ADD LEARNING =====")

        topic = input("Topic: ")
        description = input("What did you learn? ")

        while True:

            try:
                hours = float(input("Hours spent: "))
                break

            except ValueError:
                print("Please enter a valid number.")

        difficulty = input(
            "Difficulty (Easy/Medium/Hard): "
        )

        try:

            learning = LearningEntry(
                topic,
                description,
                hours,
                difficulty
            )

            self.learning_repository.add(learning)

            logger.info(
                f"Learning entry added: {topic}"
            )

            print("\nLearning entry added successfully!")

        except ValueError as error:

            print(f"\nInvalid learning entry: {error}")

            logger.warning(
                f"Invalid learning entry: {error}"
            )

    def view_learning(self):

        print("\n===== YOUR LEARNING =====")

        learning_entries = self.learning_repository.get_all()

        if not learning_entries:
            print("No learning entries found.")
            return

        for index, learning in enumerate(
            learning_entries,
            start=1
        ):
            print(f"\n[{index}]")
            learning.display()

    # ==========================================
    # PROJECTS
    # ==========================================

    def add_project(self):

        print("\n===== ADD PROJECT =====")

        name = input("Project name: ")
        description = input("Description: ")
        technology = input("Technology used: ")
        status = input("Status: ")
        priority = input("Priority (Low/Medium/High): ")

        project = Project(name, description, technology, status, priority)

        self.project_repository.add(project)
        logger.info(f"Project added: {name}")

        print("\nProject added successfully!")

    def view_projects(self):

        print("\n===== YOUR PROJECTS =====")

        projects = self.project_repository.get_all()

        if not projects:
            print("No projects found.")
            return

        for index, project in enumerate(
            projects,
            start=1
        ):
            print(f"\n[{index}]")
            project.display()


    def filter_projects(self):

        print("\n1. Planning")
        print("2. Working")
        print("3. Completed")

        choice = input("\nChoose status: ")

        status_map = {
            "1": ProjectStatus.PLANNING,
            "2": ProjectStatus.WORKING,
            "3": ProjectStatus.COMPLETED
        }

        status = status_map.get(choice)

        if status is None:
            print("\nInvalid choice.")
            return

        projects = self.project_repository.find(
            lambda project: project.status == status
        )

        if not projects:
            print("\nNo projects found.")
            return

        for project in projects:
            project.display()

    # ==========================================
    # TASKS
    # ==========================================

    def add_task(self):

        print("\n===== ADD TASK =====")

        title = input("Task: ")
        priority = input("Priority (Low/Medium/High): ")
        due_date = input("Due date (DD-MM-YYYY): ")

        try:
            datetime.strptime(due_date, "%d-%m-%Y")

        except ValueError:
            print("\nInvalid date format.")
            print("Please use DD-MM-YYYY.")
            return

        task = Task(
            title,
            priority,
            due_date
         )

        self.task_repository.add(task)
        logger.info(f"Task added: {title}")

        print("\nTask added successfully!")
    
    def view_tasks(self):

        print("\n===== YOUR TASKS =====")

        tasks = self.task_repository.get_all()

        if not tasks:
            print("No tasks found.")
            return

        for index, task in enumerate(
            tasks,
            start=1
        ):
            print(f"\n[{index}]")
            task.display()

    def complete_task(self):

        tasks = self.task_repository.get_all()

        if not tasks:
            print("\nNo tasks available.")
            return

        self.view_tasks()

        try:

            choice = int(input("\nEnter task number: "))

            task = self.task_repository.get_by_index(
                choice - 1
            )

            if task is None:
                print("\nInvalid task number.")
                return

            task.mark_completed()

            logger.info(
                f"Task completed: {task.title}"
            )

            print("\nTask marked as completed!")

        except ValueError:
            print("\nPlease enter a number.")

        except TaskAlreadyCompletedError as error:
            print(f"\n{error}")

            logger.warning(str(error))

    # ==========================================
    # EMAIL VALIDATION
    # ==========================================

    def check_email(self):

        print("\n===== EMAIL VALIDATOR =====")

        email = input("Enter email: ")

        if validate_email(email):
            print("Valid email.")

        else:
            print("Invalid email.")

    # ==========================================
    # SEARCH
    # ==========================================

    def search(self):

        print("\n===== SEARCH =====")

        keyword = input("Enter keyword: ").lower()

        found = False

        for learning in self.learning_entries:

            if keyword in learning.topic.lower():

                learning.display()
                found = True

        for project in self.projects:

            if keyword in project.name.lower():

                project.display()
                found = True

        if not found:
            print("\nNo results found.")


    # Report ------------------------------------------
    def generate_report(self):

        learning_entries = (
            self.learning_repository.get_all()
        )

        projects = self.project_repository.get_all()

        tasks = self.task_repository.get_all()

        filename = self.report_service.generate_report(
            learning_entries,
            projects,
            tasks
        )

        logger.info(
            f"Report generated: {filename}"
        )

        print("\nReport generated successfully!")
        print(f"Saved to: {filename}")




    # ==========================================
    # STATISTICS
    # ==========================================

    def statistics(self):

        print("\n===== STATISTICS =====")

        total_learning = len(self.learning_entries)
        total_projects = len(self.projects)
        total_tasks = len(self.tasks)

        completed_tasks = 0
        total_hours = 0

        for task in self.tasks:

            if task.completed:
                completed_tasks += 1

        for learning in self.learning_entries:
            total_hours += learning.hours

        print(f"Learning entries : {total_learning}")
        print(f"Projects         : {total_projects}")
        print(f"Total tasks      : {total_tasks}")
        print(f"Completed tasks  : {completed_tasks}")
        print(f"Learning hours   : {total_hours}")

    # ==========================================
    # MENU
    # ==========================================

    def menu(self):

        while True:

            print("\n===================================")
            print("             DEVTRACK")
            print("===================================")

            print("1. Add Learning")
            print("2. View Learning")
            print("3. Add Project")
            print("4. View Projects")
            print("5. Filter Projects")
            print("6. Add Task")
            print("7. View Tasks")
            print("8. Complete Task")
            print("9. Search")
            print("10. Validate Email")
            print("11. Statistics")
            print("12. Generate Report")
            print("0. Exit")

            print("===================================")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_learning()

            elif choice == "2":
                self.view_learning()

            elif choice == "3":
                self.add_project()

            elif choice == "4":
                self.view_projects()
                
            elif choice == "5":
                self.filter_projects()

            elif choice == "6":
                self.add_task()

            elif choice == "7":
                self.view_tasks()

            elif choice == "8":
                self.complete_task()

            elif choice == "9":
                self.search()

            elif choice == "10":
                self.check_email()

            elif choice == "11":
                self.statistics()
            elif choice == "12":
                self.generate_report()

            elif choice == "0":
                print("\nThank you for using DevTrack!")
                break

            else:
                print("\nInvalid choice. Try again.")
