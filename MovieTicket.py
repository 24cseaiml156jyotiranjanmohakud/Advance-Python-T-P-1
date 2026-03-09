from datetime import datetime

class Movie:
    def __init__(self, name, showtimes, price):
        self.name = name
        self.showtimes = showtimes
        self.price = price
        self.seats = {time: ["O"] * 20 for time in showtimes}


class BookingSystem:
    def __init__(self):
        self.movies = []
        self.bookings = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def check_showtimes(self):
        print("\nAvailable Movies and Showtimes:")
        for i, movie in enumerate(self.movies, 1):
            print(f"{i}. {movie.name}")
            for time in movie.showtimes:
                print(f"   - {time}")
        print()

    def display_seats(self, movie, time):
        print("\nSeat Layout (O = Available, X = Booked)")
        seats = movie.seats[time]
        for i in range(0, 20, 5):
            print(" ".join(seats[i:i+5]))
        print()

    def book_ticket(self, movie_index, time, seat_numbers):
        movie = self.movies[movie_index]
        seats = movie.seats[time]
        booked_seats = []

        for seat in seat_numbers:
            if seats[seat - 1] == "O":
                seats[seat - 1] = "X"
                booked_seats.append(seat)
            else:
                print(f"Seat {seat} already booked.")

        if booked_seats:
            total_price = len(booked_seats) * movie.price
            booking = {
                "movie": movie.name,
                "time": time,
                "seats": booked_seats,
                "total": total_price,
                "date": datetime.now()
            }
            self.bookings.append(booking)
            print("\nBooking Successful!")
            self.print_ticket(booking)
        else:
            print("No seats booked.\n")

    def print_ticket(self, booking):
        print("\n-------- MOVIE TICKET --------")
        print("Movie:", booking["movie"])
        print("Showtime:", booking["time"])
        print("Seats:", booking["seats"])
        print("Total Amount:", booking["total"])
        print("Date:", booking["date"])
        print("------------------------------\n")


system = BookingSystem()

m1 = Movie("Avengers", ["10:00 AM", "6:00 PM"], 200)
m2 = Movie("Inception", ["1:00 PM", "9:00 PM"], 180)

system.add_movie(m1)
system.add_movie(m2)

while True:
    print("Movie Ticket Booking System")
    print("1. Check Showtimes")
    print("2. Book Ticket")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        system.check_showtimes()

    elif choice == "2":
        system.check_showtimes()
        movie_choice = int(input("Select movie number: ")) - 1
        showtime = input("Enter showtime exactly as shown: ")

        movie = system.movies[movie_choice]

        if showtime not in movie.showtimes:
            print("Invalid showtime.\n")
            continue

        system.display_seats(movie, showtime)

        seats_input = input("Enter seat numbers separated by comma (1-20): ")
        seat_numbers = [int(s.strip()) for s in seats_input.split(",")]

        system.book_ticket(movie_choice, showtime, seat_numbers)

    elif choice == "3":
        print("Exiting system.")
        break

    else:
        print("Invalid choice.\n")