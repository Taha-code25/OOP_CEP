from user import User
class Admin(User):
    def __init__(self,username,email,password,firstname,lastname,balance,role,address):
        super().__init__(username,email,password,firstname,lastname,balance,role,address)
        self.balance = None
        
a1 = Admin('Ali','a@gmail.com','1719','Ali','Faisal',0000,'Admin','Germany')
a1.save_to_JSON('people.json')