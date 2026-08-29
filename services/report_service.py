from datetime import datetime


class ReportService:

    def generate_report(self, learning_entries, projects, tasks):

        filename = (
            f"reports/devtrack_report_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        )

        total_hours = 0

        for learning in learning_entries:
            total_hours += learning.hours

        completed_tasks = 0

        for task in tasks:
            if task.completed:
                completed_tasks += 1

        with open(filename, "w", encoding="utf-8") as file:

            file.write("====================================\n")
            file.write("           DEVTRACK REPORT\n")
            file.write("====================================\n\n")

            file.write(
                f"Generated: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n\n"
            )

            # --------------------------------
            # LEARNING
            # --------------------------------

            file.write("LEARNING\n")
            file.write("------------------------------------\n")

            if not learning_entries:
                file.write("No learning entries.\n")

            else:
                for entry in learning_entries:

                    file.write(
                        f"Topic: {entry.topic}\n"
                    )

                    file.write(
                        f"Description: {entry.description}\n"
                    )

                    file.write(
                        f"Hours: {entry.hours}\n"
                    )

                    file.write(
                        f"Difficulty: {entry.difficulty}\n\n"
                    )

            # --------------------------------
            # PROJECTS
            # --------------------------------

            file.write("\nPROJECTS\n")
            file.write("------------------------------------\n")

            if not projects:
                file.write("No projects.\n")

            else:
                for project in projects:

                    file.write(
                        f"Project: {project.name}\n"
                    )

                    file.write(
                        f"Technology: {project.technology}\n"
                    )

                    file.write(
                        f"Status: {project.status.value}\n"
                    )

                    file.write(
                        f"Priority: {project.priority}\n\n"
                    )

            # --------------------------------
            # TASKS
            # --------------------------------

            file.write("\nTASKS\n")
            file.write("------------------------------------\n")

            if not tasks:
                file.write("No tasks.\n")

            else:
                for task in tasks:

                    status = (
                        "Completed"
                        if task.completed
                        else "Pending"
                    )

                    file.write(
                        f"Task: {task.title}\n"
                    )

                    file.write(
                        f"Priority: {task.priority}\n"
                    )

                    file.write(
                        f"Due Date: {task.due_date}\n"
                    )

                    file.write(
                        f"Status: {status}\n\n"
                    )

            # --------------------------------
            # STATISTICS
            # --------------------------------

            file.write("\nSTATISTICS\n")
            file.write("------------------------------------\n")

            file.write(
                f"Learning entries: {len(learning_entries)}\n"
            )

            file.write(
                f"Projects: {len(projects)}\n"
            )

            file.write(
                f"Tasks: {len(tasks)}\n"
            )

            file.write(
                f"Completed tasks: {completed_tasks}\n"
            )

            file.write(
                f"Total learning hours: {total_hours}\n"
            )

        return filename