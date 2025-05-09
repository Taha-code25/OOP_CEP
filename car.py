import json
class Car:
    def  __init__(self,car_id,brand,model,seatingCapacity,rentalpricePerDay,isAvailable):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.seatingCapacity = seatingCapacity
        self.rentalPricePerDay = rentalpricePerDay
        self.isAvailable = isAvailable
    def markRented(self):
        self.isAvailable = False
    def markAvailable(self):
        self.isAvailable = True
    def to_dict(self):
        return {
            'carID': self.car_id,
            'Brand' : self.brand,
            'Model' : self.model,
            'SeatingCapacity':self.seatingCapacity,
            'Rental Price':self.rentalPricePerDay,
            'Available':self.isAvailable
        }
    def save_to_json(self,fileName):
        try:
            with open('data/'+fileName,'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []
        data.append(self.to_dict())
        with open('data/'+fileName,'w') as f:
            json.dump(data,f,indent=4)
c1 = Car('car001','Honda','Civic',4,2500,True)
c2 = Car('car002','Toyota','Corolla',4,2000,False)
c1.save_to_json('cars.json')
c2.save_to_json('cars.json')