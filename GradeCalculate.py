class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks.values())

    def calculate_percentage(self):
        total = self.calculate_total()
        return total / len(self.marks)

    def calculate_gpa(self):
        percentage = self.calculate_percentage()

        if percentage >= 90:
            return "O"
        elif percentage >= 80:
            return "E"
        elif percentage >= 70:
            return "A"
        elif percentage >= 60:
            return "B"
        elif percentage >= 50:
            return "C"
        elif percentage >= 40:
            return "D"
        else:
            return "F"

    def display_result(self):
        print("\nStudent Name:", self.name)
        print("Roll Number:", self.roll)

        print("\nMarks:")
        for subject, mark in self.marks.items():
            print(subject, ":", mark)

        print("Total Marks:", self.calculate_total())
        print("Percentage:", self.calculate_percentage())
        print("GPA:", self.calculate_gpa())


class CollegeResultSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")

        marks = {}
        n = int(input("Enter number of subjects: "))

        for i in range(n):
            subject = input("Enter subject name: ")
            mark = int(input("Enter marks: "))
            marks[subject] = mark

        student = Student(name, roll, marks)
        self.students.append(student)

    def show_results(self):
        for student in self.students:
            student.display_result()


system = CollegeResultSystem()

while True:
    print("\nCollege Result System")
    print("\n1. Add Student Marks")
    print("2. Show Results")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        system.add_student()
    elif choice == "2":
        system.show_results()
    elif choice == "3":
        break