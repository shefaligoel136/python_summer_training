class Dog:
 
 def __init__(self,name,age):
  self.name = name
  self.age  = age
  

d1 = Dog("Tuffy",3)
d2 = Dog("Noddy",2)
d3 = Dog("Tyson",5)
 
def get_oldest(o1,o2,o3):
  if o1.age>o2.age and o1.age>o3.age:
   print(o1.age,o1.name)
  elif o2.age>o3.age and o2.age>o1.age:
   print(o2.age,o2.name)
  else:
   print(o3.age,o3.name)

get_oldest(d1,d2,d3)
