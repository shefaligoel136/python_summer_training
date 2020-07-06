class a:
 def greet(self):
  #super().greet()
  print("A says Hello")
 
class b(a):
 def greet(self):
  super().greet()
  print("B says Hello")
  
class c(b):
 def greet(self):
  super().greet()
  print("C says Hello")
obj = c()
obj.greet()