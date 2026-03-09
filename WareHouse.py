#Warehouse Automation System(Trak goods movement, generate inventory reports and forecast demand)

class Product:

    def __init__(self, name, quantity):
        self._name = name
        self._quantity = quantity

    def get_name(self):
        return self._name

    def get_quantity(self):
        return self._quantity

    def add_stock(self, amount):
        self._quantity += amount

    def remove_stock(self, amount):
        if amount <= self._quantity:
            self._quantity -= amount
        else:
            print("Not enough stock")


class Inventory(Product):

    def __init__(self, name, quantity):
        super().__init__(name, quantity)
        self._movement_log = []

    def track_incoming(self, amount):
        self.add_stock(amount)
        self._movement_log.append("Added " + str(amount) + " units")

    def track_outgoing(self, amount):
        if amount <= self._quantity:
            self.remove_stock(amount)
            self._movement_log.append("Removed " + str(amount) + " units")
        else:
            print("Insufficient stock")

    def show_movements(self):
        if self._movement_log:
            for log in self._movement_log:
                print(log)
        else:
            print("No movements recorded")


class Report:

    def generate_report(self, products):
        print("\nInventory Report")
        for p in products:
            print("Product:", p.get_name(), "| Stock:", p.get_quantity())


class DemandForecast:

    def forecast(self, products):
        print("\nDemand Forecast")
        for p in products:
            if p.get_quantity() < 20:
                print(p.get_name(), "→ High demand expected")
            else:
                print(p.get_name(), "→ Stock sufficient")


products = []

while True:

    print("\nWarehouse Automation System")
    print("1 Add Product")
    print("2 Add Stock")
    print("3 Remove Stock")
    print("4 Track Movements")
    print("5 Generate Inventory Report")
    print("6 Forecast Demand")
    print("7 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Product Name: ")
        quantity = int(input("Initial Quantity: "))
        p = Inventory(name, quantity)
        products.append(p)
        print("Product added")

    elif choice == "2":
        name = input("Product Name: ")
        amount = int(input("Stock to add: "))

        for p in products:
            if p.get_name() == name:
                p.track_incoming(amount)

    elif choice == "3":
        name = input("Product Name: ")
        amount = int(input("Stock to remove: "))

        for p in products:
            if p.get_name() == name:
                p.track_outgoing(amount)

    elif choice == "4":
        name = input("Product Name: ")

        for p in products:
            if p.get_name() == name:
                p.show_movements()

    elif choice == "5":
        report = Report()
        report.generate_report(products)

    elif choice == "6":
        forecast = DemandForecast()
        forecast.forecast(products)

    elif choice == "7":
        break

    else:
        print("Invalid choice")