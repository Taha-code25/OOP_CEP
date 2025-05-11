from user import User
from car import Car
import json
import os
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
        file_path = f"data/{file_name}"
        
        try:
            # Load existing history if file exists and is not empty
            if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                with open(file_path, "r") as f:
                    existing_data = json.load(f)
            else:
                existing_data = []

            # Merge new records
            existing_data.extend(self.rental_history)

            # Write full list back to file
            with open(file_path, "w") as f:
                json.dump(existing_data, f, indent=4)

            # Clear in-memory history after saving
            self.rental_history.clear()
            print("Rental history saved to file.")

        except Exception as e:
            print(f"Error saving rental history: {e}")

        except Exception as e:
            print(f"Error saving rental history: {e}")
            
            
    def view_user_rental_history(self, username, file_name='rental_history.json'):
        if username not in self.users:
            return f"User '{username}' not found."

        file_path = f"data/{file_name}"

        try:
            # Load history from file
            if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                with open(file_path, "r") as f:
                    full_history = json.load(f)
            else:
                full_history = []
        except Exception as e:
            return  f"Error loading rental history: {e}"

        # Filter user's records
        user_history = [record for record in full_history if record["username"] == username]

        if not user_history:
            return f"No rental history found for user '{username}'."

    

        return user_history
            


system2 = Rental_System()
faisal = User("faisal", "umer@mail.com", "pass", "Umer", "Ali", 50000, "customer", "Lahore")
system2.add_user(faisal)
toyota = Car("car002", "Toyota", "Corolla", 4, 2500, True)
system2.add_car(toyota)
start = datetime(2025, 5, 6)
end = datetime(2025, 5, 9)  # 3 days
system2.reserve_car("faisal", "car002", start, end)
print(f"\nRemaining balance: ${faisal.balance}")
system2.save_rental_history()
print(system2.view_user_rental_history("faisal"))
