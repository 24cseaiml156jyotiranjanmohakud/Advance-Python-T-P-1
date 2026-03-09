from datetime import datetime

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class BillingSystem:
    def __init__(self):
        self.cart = []
        self.transactions = []

    def scan_product(self, product, quantity):
        self.cart.append((product, quantity))
        print(f"{product.name} added to cart.\n")

    def apply_discount(self, total, discount_percent):
        discount_amount = total * (discount_percent / 100)
        return total - discount_amount

    def generate_bill(self, discount_percent=0):
        if not self.cart:
            print("Cart is empty.\n")
            return

        print("\n-------- BILL --------")
        total = 0

        for product, quantity in self.cart:
            item_total = product.price * quantity
            total += item_total
            print(f"{product.name} x {quantity} = {item_total}")

        print("----------------------")
        print("Subtotal:", total)

        if discount_percent > 0:
            total = self.apply_discount(total, discount_percent)
            print("Discount Applied:", discount_percent, "%")

        print("Final Total:", total)
        print("----------------------")

        transaction = {
            "date": datetime.now(),
            "items": self.cart.copy(),
            "total": total
        }

        self.transactions.append(transaction)
        self.cart.clear()
        print("Transaction recorded.\n")

    def show_transactions(self):
        if not self.transactions:
            print("No transactions found.\n")
            return

        for i, trans in enumerate(self.transactions, 1):
            print(f"\nTransaction {i}")
            print("Date:", trans["date"])
            for product, quantity in trans["items"]:
                print(f"{product.name} x {quantity}")
            print("Total:", trans["total"])
            print("----------------------")

p1 = Product("Milk", 50)
p2 = Product("Bread", 30)
p3 = Product("Rice", 60)
p4 = Product("Sugar", 45)

billing = BillingSystem()

while True:
    print("Retail Billing System")
    print("1. Scan Product")
    print("2. Generate Bill")
    print("3. Show Transactions")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Available Products:")
        print("1. Milk - 50")
        print("2. Bread - 30")
        print("3. Rice - 60")
        print("4. Sugar - 45")

        product_choice = input("Select product number: ")
        quantity = float(input("Enter quantity in (g/kg): "))

        if product_choice == "1":
            billing.scan_product(p1, quantity)
        elif product_choice == "2":
            billing.scan_product(p2, quantity)
        elif product_choice == "3":
            billing.scan_product(p3, quantity)
        elif product_choice == "4":
            billing.scan_product(p4, quantity)
        else:
            print("Invalid product.\n")

    elif choice == "2":
        discount = float(input("Enter discount percentage (0 if none): "))
        billing.generate_bill(discount)

    elif choice == "3":
        billing.show_transactions()

    elif choice == "4":
        print("Exiting system.")
        break

    else:
        print("Invalid choice.\n")