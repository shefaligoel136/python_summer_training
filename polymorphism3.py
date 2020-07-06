#duck typing

class Duck:
 def fly(self):
  print("duck is flying") 

class Airplane:
 def fly(self):
  print("Airplane is flying") 

class Car:
 def run(self):
  print("car is running") 
  
def check(property):
 property.fly()

duck = Duck()
airplane = Airplane()
car = Car()

check(duck)