class RoomAllotmentSystem:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room_number):
        if room_number in self.rooms:
            print("Room already exists!")
        else:
            self.rooms[room_number] = None
            print(f"Room {room_number} added successfully!")

    def allot_room(self, room_number, student_name):
        if room_number not in self.rooms:
            print("Room does not exist!")
        elif self.rooms[room_number] is not None:
            print("Room already allotted!")
        else:
            self.rooms[room_number] = student_name
            print(f"Room {room_number} allotted to {student_name}!")

    def vacate_room(self, room_number):
        if room_number not in self.rooms:
            print("Room does not exist!")
        elif self.rooms[room_number] is None:
            print("Room is already vacant!")
        else:
            print(f"Room {room_number} vacated from {self.rooms[room_number]}")
            self.rooms[room_number] = None

    def display_rooms(self):
        print("\nRoom Status:")
        for room, student in self.rooms.items():
            if student is None:
                print(f"Room {room} -> Vacant")
            else:
                print(f"Room {room} -> Allotted to {student}")
        print()

ras=RoomAllotmentSystem()

while True:
    print("===== Room Allotment System =====")
    print("1. Add Room")
    print("2. Allot Room")
    print("3. Vacate Room")
    print("4. Display Rooms")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        room = input("Enter room number: ")
        ras.add_room(room)

    elif choice == "2":
        room = input("Enter room number: ")
        name = input("Enter student name: ")
        ras.allot_room(room, name)

    elif choice == "3":
        room = input("Enter room number: ")
        ras.vacate_room(room)

    elif choice == "4":
        ras.display_rooms()

    elif choice == "5":
        print("Thank You for visiting into our system, See you again@")
        break

    else:
        print("Invalid choice! Try again.")