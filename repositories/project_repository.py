from repositories.base_repository import BaseRepository


class ProjectRepository(BaseRepository):

    def __init__(self):
        self.projects = []

    def add(self, project):
        self.projects.append(project)

    def get_all(self):
        return self.projects

    def find_by_status(self, status):

        results = []

        for project in self.projects:

            if project.status == status:
                results.append(project)

        return results