from datetime import datetime
from models.learning import LearningEntry
from models.project import Project
from models.task import Task
from utils.valiadators import validate_email


class DevTrack:

    def __init__(self):
        self.learning_entries = []
        self.projects = []
        self.tasks = []

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

        difficulty = input("Difficulty (Easy/Medium/Hard): ")

        learning = LearningEntry(topic, description, hours, difficulty)

        self.learning_entries.append(learning)

        print("\nLearning entry added successfully!")

    def view_learning(self):

        print("\n===== YOUR LEARNING =====")

        if not self.learning_entries:
            print("No learning entries found.")
            return

        for index, learning in enumerate(self.learning_entries, start=1):
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

        self.projects.append(project)

        print("\nProject added successfully!")

    def view_projects(self):

        print("\n===== YOUR PROJECTS =====")

        if not self.projects:
            print("No projects found.")
            return

        for index, project in enumerate(self.projects, start=1):
            print(f"\n[{index}]")
            project.display()


    def filter_projects(self):

        print("\n===== FILTER PROJECTS =====")

        status = input(
            "Enter status (Planning/Working/Completed): "
        ).lower()

        found = False

        for project in self.projects:

            if project.status.lower() == status:
                project.display()
                found = True

        if not found:
            print("\nNo projects found with this status.")

        for project in self.projects:

            if project.status.lower() == status:
                project.display()
                found = True

        if not found:
            print("\nNo projects found with this status.")

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

        self.tasks.append(task)

        print("\nTask added successfully!")
    
    def view_tasks(self):

        print("\n===== YOUR TASKS =====")

        if not self.tasks:
            print("No tasks found.")
            return

        for index, task in enumerate(self.tasks, start=1):
            print(f"\n[{index}]")
            task.display()

    def complete_task(self):

        if not self.tasks:
            print("\nNo tasks available.")
            return

        self.view_tasks()

        try:
            choice = int(input("\nEnter task number: "))

            if 1 <= choice <= len(self.tasks):
                self.tasks[choice - 1].mark_completed()
                print("\nTask marked as completed!")

            else:
                print("\nInvalid task number.")

        except ValueError:
            print("\nPlease enter a number.")

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

            elif choice == "0":
                print("\nThank you for using DevTrack!")
                break

            else:
                print("\nInvalid choice. Try again.")
