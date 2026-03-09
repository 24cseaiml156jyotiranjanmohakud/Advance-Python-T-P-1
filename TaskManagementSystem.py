from datetime import datetime

class Task:
    def __init__(self, title, deadline, priority, project_tag):
        self.title = title
        self.deadline = deadline
        self.priority = priority
        self.project_tag = project_tag
        self.status = "Pending"

    def mark_completed(self):
        self.status = "Completed"

    def display(self):
        print("Title:", self.title)
        print("Deadline:", self.deadline)
        print("Priority:", self.priority)
        print("Project Tag:", self.project_tag)
        print("Status:", self.status)
        print("-" * 30)


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, deadline, priority, project_tag):
        task = Task(title, deadline, priority, project_tag)
        self.tasks.append(task)
        print("Task added successfully.\n")

    def display_all_tasks(self):
        if not self.tasks:
            print("No tasks available.\n")
        else:
            for task in self.tasks:
                task.display()

    def filter_by_project(self, tag):
        found = False
        for task in self.tasks:
            if task.project_tag.lower() == tag.lower():
                task.display()
                found = True
        if not found:
            print("No tasks found for this project.\n")

    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                task.mark_completed()
                print("Task marked as completed.\n")
                return
        print("Task not found.\n")

    def remove_task(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                self.tasks.remove(task)
                print("Task removed successfully.\n")
                return
        print("Task not found.\n")


todo = ToDoList()

while True:
    print("To-Do-List Menu")
    print("1. Add Task")
    print("2. Display All Tasks")
    print("3. Filter by Project Tag")
    print("4. Mark Task as Completed")
    print("5. Remove Task")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter task: ")
        deadline = input("Enter deadline (YYYY-MM-DD): ")
        priority = input("Enter priority (High/Medium/Low): ")
        project_tag = input("Enter project tag: ")
        todo.add_task(title, deadline, priority, project_tag)

    elif choice == "2":
        todo.display_all_tasks()

    elif choice == "3":
        tag = input("Enter project tag to filter: ")
        todo.filter_by_project(tag)

    elif choice == "4":
        title = input("Enter task title to mark completed: ")
        todo.mark_task_completed(title)

    elif choice == "5":
        title = input("Enter task title to remove: ")
        todo.remove_task(title)

    elif choice == "6":
        print("Exiting program.")
        break

    else:
        print("Invalid choice.\n")