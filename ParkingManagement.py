from datetime import datetime


class Vehicle:
    def __init__(self, number, vtype):
        self.number = number
        self.vtype = vtype
        self.entry_time = datetime.now()


class ParkingLot:
    def __init__(self, total_spots):
        self.total_spots = total_spots
        self.available_spots = total_spots
        self.vehicles = {}

    def entry(self):
        if self.available_spots == 0:
            print("Parking Full")
            return

        number = input("Enter vehicle number: ")
        vtype = input("Enter vehicle type (2/4): ")

        vehicle = Vehicle(number, vtype)
        self.vehicles[number] = vehicle
        self.available_spots -= 1

        print("Vehicle Parked Successfully")
        print("Entry Time:", vehicle.entry_time.strftime("%Y-%m-%d %H:%M:%S"))
        print("Available spots:", self.available_spots)

    def exit(self):
        number = input("Enter vehicle number: ")

        if number not in self.vehicles:
            print("Vehicle not found")
            return

        vehicle = self.vehicles[number]
        exit_time = datetime.now()

        time_difference = exit_time - vehicle.entry_time
        hours = time_difference.total_seconds() / 3600

        if vehicle.vtype == "2":
            fee = hours * 10
        else:
            fee = hours * 20

        print("Vehicle Number:", vehicle.number)
        print("Entry Time:", vehicle.entry_time.strftime("%Y-%m-%d %H:%M:%S"))
        print("Exit Time:", exit_time.strftime("%Y-%m-%d %H:%M:%S"))
        print("Total Hours:", round(hours, 2))
        print("Parking Fee:", round(fee, 2))

        del self.vehicles[number]
        self.available_spots += 1

        print("Vehicle Exited Successfully")
        print("Available spots:", self.available_spots)

    def show_available(self):
        print("Total Spots:", self.total_spots)
        print("Available Spots:", self.available_spots)

    def show_vehicles(self):
        if len(self.vehicles) == 0:
            print("No vehicles parked")
        else:
            for number in self.vehicles:
                print("Vehicle Number:", number)


parking = ParkingLot(5)

while True:
    print("\n1. Vehicle Entry")
    print("2. Vehicle Exit")
    print("3. Show Available Spots")
    print("4. Show Parked Vehicles")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        parking.entry()
    elif choice == "2":
        parking.exit()
    elif choice == "3":
        parking.show_available()
    elif choice == "4":
        parking.show_vehicles()
    elif choice == "5":
        print("Thank You")
        break
    else:
        print("Invalid Choice")