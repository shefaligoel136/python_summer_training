class person:
 def a(self,name,age):
  self.a = name
  self.c = age
 
 def b(self):
  print("hi",self.a)
  print("age is",self.c)
  
 def c(self):
  print("your info")

obj = person()
obj.c()
obj.a("shefali",19)  
obj.b()
print(obj.c)
