from auth import Auth
from user import User
from admin import Admin
from car import Car
from rental_system import Rental_System
from datetime import datetime
from fileLoad import LoadData
# Initialize system
rental_system = Rental_System()
auth = Auth()

def admin_menu(admin):
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Car")
        print("2. Remove Car")
        print("3. View Reserved Cars")
        print("4. View Rental History")
        print("5. Logout")
        choice = input("Choose an option: ")

        if choice == "1":
            car_id = input("Car ID: ")
            brand = input("Brand: ")
            model = input("Model: ")
            seating = int(input("Seating Capacity: "))
            price = float(input("Rental Price per Day: "))
            is_available = True
            try:
                admin.add_car_to_system(car_id, brand, model, seating, price, is_available)
            except ValueError as e:
                print(e)
        elif choice == "2":
            car_id = input("Car ID to remove: ")
            admin.remove_car_from_system(car_id)
        elif choice == "3":
            reserved = admin.print_reserved_cars()
            print("Reserved Cars:", reserved)
        elif choice == "4":
            history = admin.print_rental_history()
            for record in history:
                print(record)
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid choice.")

def customer_menu(user):
    rental_system.add_user(user)
    while True:
        print("\n--- Customer Menu ---")
        print("1. Rent a Car")
        print("2. Return Car")
        print("3. View Rental History")
        print("4. Logout")
        choice = input("Choose an option: ")

        if choice == "1":
            car_id = input("Car ID to rent: ")
            brand = input("Car Brand (for loading purpose): ")
            model = input("Car Model: ")
            seating = int(input("Seating Capacity: "))
            price = float(input("Price/Day: "))
            is_available = True
            car = Car(car_id, brand, model, seating, price, is_available)
            rental_system.add_car(car)

            try:
                start_date = datetime.strptime(input("Start date (YYYY-MM-DD): "), "%Y-%m-%d")
                end_date = datetime.strptime(input("End date (YYYY-MM-DD): "), "%Y-%m-%d")
                rental_system.reserve_car(user.username, car_id, start_date, end_date)
                rental_system.save_rental_history()
            except Exception as e:
                print("Error:", e)

        elif choice == "2":
            print(rental_system.return_car(user.username))
        elif choice == "3":
            history = rental_system.view_user_rental_history(user.username)
            print(history)
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid choice.")

def main():
    print("=== Welcome to Car Rental CLI ===")
    while True:
        print("\n1. Sign In\n2. Sign Up\n3. Exit")
        option = input("Choose an option: ")

        if option == "1":
            username = input("Username: ")
            password = input("Password: ")
            if auth.signIN(username, password):
                print("Sign In Successful.")
                data = Auth().signIN(username, password)
                user_data = [u for u in LoadData().loadData() if u['Username'] == username][0]
                if user_data["Role"].lower() == "admin":
                    admin = Admin(**user_data)
                    admin_menu(admin)
                else:
                    user = User(**user_data)
                    customer_menu(user)
            else:
                print("Invalid credentials.")

        elif option == "2":
            print("\n--- Sign Up ---")
            username = input("Username: ")
            email = input("Email: ")
            password = input("Password: ")
            fname = input("First Name: ")
            lname = input("Last Name: ")
            balance = float(input("Initial Balance: "))
            role = input("Role (admin/customer): ")
            address = input("Address: ")
            if auth.signUP(username, email, password, fname, lname, balance, role, address):
                print("Registration successful. You can now log in.")
            else:
                print("Sign up failed.")
        elif option == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
