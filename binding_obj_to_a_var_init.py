class person:
 def __init__(self,name,age):
  self.a = name
  self.c = age
 
 def b(self):
  print("hi",self.a)
  print("age is",self.c)

 def info(self,k):
  print("your info",k)
  
obj = person("shefali",19)
obj.info(obj.a)  
obj.b()
print(obj.c)