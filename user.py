import json
from car import Car
class User:
    def __init__(self,username,email,password,firstname,lastname,balance,role,address):
        self.username = username
        self.email = email
        self.password = password
        self.firstName = firstname
        self.lastName = lastname
        self.balance = balance
        self.role = role
        self.address = address
<<<<<<< HEAD
##################3 Umers part ################
        self.rented_car_id = None
        
=======
        self.rentalHistory = []
>>>>>>> fa0c7083ef04a7e0dd0916ebf89768c31d0bfc0a
    def to_dict(self):
            return {
                'Username':self.username,
                'Email':self.email,
                'Password': self.password,
                'FirstName':self.firstName,
                'LastName':self.lastName,
                'Balance':self.balance,
                'Role':self.role,
<<<<<<< HEAD
                'Address':self.address,
                'RentedCarID': self.rented_car_id

                }
=======
                'Address':self.address
                 }
>>>>>>> fa0c7083ef04a7e0dd0916ebf89768c31d0bfc0a
    def save_to_JSON(self,fileName):
            try:
                with open('data/'+fileName,'r') as f:
                    data = json.load(f)
            except FileNotFoundError:
                data = []
            data.append(self.to_dict())
            with open('data/'+fileName,'w') as f:
                json.dump(data, f, indent=4)
<<<<<<< HEAD
                
##################3 Umers part ################
    def has_rented_a_car(self):
        if self.rented_car_id is not None:
            return True
        else:
            return False
    def return_car(self):
        self.rented_card_id=None
    def rent_a_car(self,car_id):
        self.rented_card_id=car_id
=======

>>>>>>> fa0c7083ef04a7e0dd0916ebf89768c31d0bfc0a
# person1 = User('Taha Faisal','taha@g.com','3675','Taha','Faisal','6900','Admin','Tere Ghar')
# person1.save_to_JSON('data/people.json')