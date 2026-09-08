from utils.status import ProjectStatus


class Project:

    def __init__(self, name, description, technology, status, priority):
        self.name = name
        self.description = description
        self.technology = technology
        # Keep the status as an enum inside the application.  JSON can only
        # represent simple values, so ``to_dict`` converts it to its text
        # value when it is written to disk.
        self.status = (
            status
            if isinstance(status, ProjectStatus)
            else ProjectStatus(status.capitalize())
        )
        self.priority = priority

    def to_dict(self) -> dict:
        """Return a JSON-safe representation of this project."""
        return {
            "name": self.name,
            "description": self.description,
            "technology": self.technology,
            "status": self.status.value,
            "priority": self.priority,
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Recreate a project, including its ``ProjectStatus`` enum."""
        return cls(
            data["name"],
            data["description"],
            data["technology"],
            ProjectStatus(data["status"]),
            data["priority"],
        )

    def display(self):
        print("\n-----------------------------")
        print(f"Project     : {self.name}")
        print(f"Description : {self.description}")
        print(f"Technology  : {self.technology}")
        print(f"Status      : {self.status.value}")
        print(f"Priority    : {self.priority}")
        print("-----------------------------")
