class Project:
    def __init__(self, name, description, technology, status):
        self.name = name
        self.description = description
        self.technology = technology
        self.status = status

    def display(self):
        print("\n-----------------------------")
        print(f"Project     : {self.name}")
        print(f"Description : {self.description}")
        print(f"Technology  : {self.technology}")
        print(f"Status      : {self.status}")
        print("-----------------------------")