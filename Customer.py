#Customer Relationship Manager(core customer info,mange communication logs and track sales pipeline)

class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def get_info(self):
        return f"Name: {self.name}\nEmail: {self.email}\nPhone: {self.phone}"

class Customer(Person):
    def __init__(self, name, email, phone, company):
        super().__init__(name, email, phone)
        self._company = company
        self._communications = []
        self._sales_stage = "Lead"
    
    def add_communication(self, message):
        self._communications.append(message)

    def show_communications(self):
        if self._communications:
            for msg in self._communications:
                print(msg)
        else:
            print("No communication records")

    def update_sales_stage(self, stage):
        self._sales_stage = stage

    def show_sales_stage(self):
        print("Sales Stage:", self._sales_stage)

    def show_customer(self):
        print(self.get_details())
        print("Company:", self._company)



customers = []

while True:

    print("\nCustomer Relationship Manager")
    print("1 Add Customer")
    print("2 Show Customers")
    print("3 Add Communication")
    print("4 Show Communications")
    print("5 Update Sales Stage")
    print("6 Show Sales Stage")
    print("7 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone: ")
        company = input("Company: ")

        c = Customer(name, email, phone, company)
        customers.append(c)
        print("Customer added")

    elif choice == "2":
        for c in customers:
            c.show_customer()

    elif choice == "3":
        name = input("Enter customer name: ")
        for c in customers:
            if c._name == name:
                message = input("Enter communication log: ")
                c.add_communication(message)

    elif choice == "4":
        name = input("Enter customer name: ")
        for c in customers:
            if c._name == name:
                c.show_communications()

    elif choice == "5":
        name = input("Enter customer name: ")
        for c in customers:
            if c._name == name:
                stage = input("Enter sales stage (Lead/Negotiation/Closed): ")
                c.update_sales_stage(stage)

    elif choice == "6":
        name = input("Enter customer name: ")
        for c in customers:
            if c._name == name:
                c.show_sales_stage()

    elif choice == "7":
        break

    else:
        print("Invalid choice")