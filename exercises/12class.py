class class_name:
   # pass (used to create empty class or functions)
   def __init__(self):
      print("class is being created ")


obj1 = class_name()
obj1.id = "001"

print(obj1.id)

class user:
    def __init__ (self,user_id,username):
      self.id = user_id
      self.username = username

user_1 = user("001","angela")

print(user_1.id,user_1.username)

class car:
    def __init__(self):
        self.seats = "4"
    def enter_race_mode(self):
        self.seats = "2"
   
my_car = car()
print(my_car.seats)
my_car.enter_race_mode()
print(my_car.seats)