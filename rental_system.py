from user import User
from car import Car
import json
from datetime import datetime
class Rental_System:
    def __init__(self):
        self.users={}
        self.cars={}
        self.rental_history=[]
        
    def add_car(self, car:Car):
        self.cars[car.car_id]=car
        
    def add_user(self,user:User):
        self.users[user.username]=user
        
    def reserve_car(self,username, car_id, start_date,end_date):
        if username not in self.users:
            return f'{username} not found!'
        user=self.users[username]
        car=self.cars.get(car_id)
        
        # Check if user exists
        if not user:
            raise ValueError(f"User '{username}' not found.")
    
        # Check if car exists
        if not car:
            raise ValueError(f"Car ID '{car_id}' not found.")
        
        if user.has_rented_a_car():                     # Ensure user doesn't already have an active rental
            raise Exception("User already has a rented car.")
        
        if not car.isAvailable:                        # Ensure the car is available for rental
            raise Exception(f"Car '{car.model}' is not available.")
        
        # Validate inputs
        if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
            raise ValueError("Start and end dates must be datetime objects.")
        
        
        if start_date >= end_date:                    # Ensure the rental period is valid
            raise ValueError("End date must be after start date.")
        
         
        total_days = (end_date - start_date).days      # Calculate rental cost
        total_cost = total_days * car.rentalPricePerDay

        if user.balance < total_cost:                # Ensure user has enough balance
            raise Exception("Insufficient balance to reserve this car.")
        
        # Deduct balance
        user.balance -= total_cost
        
        #record rental
        rental_record = {
            "username": user.username,
            "email": user.email,
            "car_id": car.car_id,
            "brand": car.brand,
            "model": car.model,
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
            "total_days": total_days,
            "total_cost": total_cost
        }
        self.rental_history.append(rental_record)
        
        
       # Mark the car as rented and update user record
        user.rent_a_car(car_id)  # Save car ID to user
        car.markRented()         # Set availability to False
        
        print(f"Car '{car.model}' reserved successfully for Rs:{total_cost}")
        return True
    
    def return_car(self, username):
        if username not in self.users:                   # Check if user exists
            return f'{username} not found!'
        user=self.users[username]
        if not user.has_rented_a_car():                  # Check if user has an active rental
            return f'The user has not rented any car yet!'
        
        # Get the car ID and object
        car_id=user.rented_car_id
        car=self.cars.get(car_id)
        
        if car:
            car.markAvailable()                           # Mark car available if it exists
        user.return_car()                                 # Remove rental from user's record
        return f'{username} returned the car with Car ID: {car_id}'
    
    def save_rental_history(self, file_name='rental_history.json'):
        try:
            with open(f"data/{file_name}", "w") as f:
                    json.dump(self.rental_history, f, indent=4)
        except Exception as e:
            print(f"Error saving rental history: {e}")

    
# system = Rental_System()
# umer = User("umer123", "umer@mail.com", "pass", "Umer", "Ali", 10000, "customer", "Lahore")
# system.add_user(umer)
# civic = Car("car001", "Honda", "Civic", 4, 2500, True)
# system.add_car(civic)
# start = datetime(2025, 5, 6)
# end = datetime(2025, 5, 9)  # 3 days
# system.reserve_car("umer123", "car001", start, end)
# print("\nRental History:")
# for record in system.rental_history:
#         print(record)
# print(f"\nRemaining balance: ${umer.balance}")