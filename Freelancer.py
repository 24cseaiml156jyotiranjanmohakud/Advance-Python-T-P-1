#Freelance Marketplace Simulation(register freelancer and clients, assign project, and process payments)

class User:

    def __init__(self, name, email):
        self._name = name
        self._email = email

    def get_name(self):
        return self._name

    def get_details(self):
        return "Name: " + self._name + " | Email: " + self._email


class Freelancer(User):

    def __init__(self, name, email, skill):
        super().__init__(name, email)
        self._skill = skill
        self._projects=[]

    def add_project(self, project):
        self._projects.append(project)

    def show_projects(self):
        if self._projects:
            for p in self._projects:
                print(p.get_title())
        else:
            print("No projects assigned")


class Client(User):

    def __init__(self, name, email):
        super().__init__(name, email)

    def create_project(self, title, budget):
        project = Project(title, budget, self._name)
        return project


class Project:

    def __init__(self, title, budget, client):
        self._title = title
        self._budget = budget
        self._client = client
        self._freelancer = None
        self._status = "Open"

    def assign_freelancer(self, freelancer):
        self._freelancer = freelancer
        freelancer.add_project(self)
        self._status = "Assigned"

    def complete_project(self):
        self._status = "Completed"

    def get_title(self):
        return self._title

    def get_status(self):
        return self._status

    def get_budget(self):
        return self._budget

    def get_freelancer(self):
        return self._freelancer


class Payment:

    def process_payment(self, project):
        if project.get_status() == "Completed":
            freelancer = project.get_freelancer()
            print("Payment of", project.get_budget(), "paid to", freelancer.get_name())
        else:
            print("Project not completed. Payment cannot be processed.")


freelancers = []
clients = []
projects = []

while True:

    print("\nFreelance Marketplace")
    print("1 Register Freelancer")
    print("2 Register Client")
    print("3 Create Project")
    print("4 Assign Project")
    print("5 Complete Project")
    print("6 Process Payment")
    print("7 Show Freelancers")
    print("8 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Freelancer Name: ")
        email = input("Email: ")
        skill = input("Skill: ")

        f = Freelancer(name, email, skill)
        freelancers.append(f)

        print("Freelancer registered")

    elif choice == "2":
        name = input("Client Name: ")
        email = input("Email: ")

        c = Client(name, email)
        clients.append(c)

        print("Client registered")

    elif choice == "3":
        client_name = input("Client Name: ")
        title = input("Project Title: ")
        budget = int(input("Budget: "))

        for c in clients:
            if c.get_name() == client_name:
                p = c.create_project(title, budget)
                projects.append(p)
                print("Project created")

    elif choice == "4":
        title = input("Project Title: ")
        freelancer_name = input("Freelancer Name: ")

        for p in projects:
            if p.get_title() == title:
                for f in freelancers:
                    if f.get_name() == freelancer_name:
                        p.assign_freelancer(f)
                        print("Project assigned")

    elif choice == "5":
        title = input("Project Title: ")

        for p in projects:
            if p.get_title() == title:
                p.complete_project()
                print("Project completed")

    elif choice == "6":
        title = input("Project Title: ")
        pay = Payment()

        for p in projects:
            if p.get_title() == title:
                pay.process_payment(p)

    elif choice == "7":
        for f in freelancers:
            print(f.get_details())

    elif choice == "8":
        break

    else:
        print("Invalid choice")