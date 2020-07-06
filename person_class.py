class person:
 def info(self,name,age):
  print("my name is {} and i am {} years old".format(name,age))
  print(f"my name is {name} and i am {age} years old")

obj1 = person()
obj2 = person()

obj1.info("abc",10)
obj2.info("xyz",12)
person.info(obj1,"ghh",14)
