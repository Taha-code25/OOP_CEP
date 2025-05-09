from user import User
from car import Car
import json
class Admin(User):
    def __init__(self,username,email,password,firstname,lastname,balance,role,address):
        super().__init__(username,email,password,firstname,lastname,balance,role,address)
        self.balance = None
    def add_car_to_system(self,car_id,brand,model,seatingCapacity,rentalpricePerDay,isAvailable):
        try:
            with open('data/cars.json','r') as f:
                data  = json.load(f)
        except FileNotFoundError as e:
            data = []
        for car in data:
            if car.get('carID') == car_id:
                raise ValueError("Car already exists!")
        new_car = {
            'carID':car_id,
            'Brand':brand,
            "Model": model,
            "SeatingCapacity": seatingCapacity,
            "Rental Price": rentalpricePerDay,
            "Available": isAvailable
        }
        data.append(new_car)
        with open('data/cars.json','w') as f:
            json.dump(data,f,indent=4)
        print(f'Car {car_id} added succesfully!')
    def remove_car_from_system(self,car_id):
        try:
            with open('data/cars.json','r') as f:
                data  = json.load(f)
        except FileNotFoundError:
            print("File Not Found!")
        if not any (car.get('carID') == car_id for car in data):
               raise ValueError('Car doesn\'t exist!')
        for car in data:
            if car.get('carID') == car_id:
                data.remove(car)
        with open('data/cars.json','w') as f:
            json.dump(data,f,indent=4)
        print(f'Car {car_id} removed succesfully!')
    def print_reserved_cars(self):
        try:
            with open('data/cars.json','r') as f:
                data = json.load(f)
                reserved_cars = []
                for car in data:
                    if car.get('isAvaialable') == False:
                        reserved_cars.append(car)
                return reserved_cars
        except FileNotFoundError:
            print("File not found!")
        
    



    
a1 = Admin('Ali','a@gmail.com','1719','Ali','Faisal',0000,'Admin','Germany')
a1.save_to_JSON('people.json')
# a1.add_car_to_system('bkl-420','Toyota','Corolla',4,250,True)
# a1.add_car_to_system('bkl-2024','Toyota','Corolla',4,250,True)
a1.remove_car_from_system('car001')