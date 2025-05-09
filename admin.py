from user import User
from car import Car
import json

class Admin(User):
    def __init__(self, username, email, password, firstname, lastname, balance, role, address):
        super().__init__(username, email, password, firstname, lastname, balance, role, address)
        self.balance = None  # Keeping balance as it may be used later

    def add_car_to_system(self, car_id, brand, model, seating_capacity, rental_price_per_day, is_available):
        try:
            with open('data/cars.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        for car in data:
            if car.get('carID') == car_id:
                raise ValueError("Car already exists!")
        
        new_car = {
            'carID': car_id,
            'Brand': brand,
            'Model': model,
            'SeatingCapacity': seating_capacity,
            'RentalPricePerDay': rental_price_per_day,
            'Available': is_available
        }
        data.append(new_car)
        with open('data/cars.json', 'w') as f:
            json.dump(data, f, indent=4)
        print(f'Car {car_id} added successfully!')

    def remove_car_from_system(self, car_id):
        try:
            with open('data/cars.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            print("File not found!")
            return

        car_exists = False
        for car in data:
            if car.get('carID') == car_id:
                car_exists = True
                data.remove(car)
                break

        if not car_exists:
            print(f"Car with ID {car_id} doesn't exist!")
            return

        with open('data/cars.json', 'w') as f:
            json.dump(data, f, indent=4)
        
        print(f'Car {car_id} removed successfully!')

    def print_reserved_cars(self):
        try:
            with open('data/cars.json', 'r') as f:
                data = json.load(f)
                reserved_cars = [car for car in data if not car.get('Available')]  # Checking the correct field name 'Available'
                return reserved_cars
        except FileNotFoundError:
            print("File not found!")

# Example usage
a1 = Admin('Ali', 'a@gmail.com', '1719', 'Ali', 'Faisal', 0, 'Admin', 'Germany')
a1.save_to_JSON('people.json')

try:
    a1.remove_car_from_system('car002')
except ValueError as e:
    print("Error:", e)

