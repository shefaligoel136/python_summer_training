class b:
 def k(self):
  print("this is k func")
  
class a:
 def a(self,obj2):
  obj2.k()
 
class d:
 def k(self):
  print("this is k in d")

obj2 = d()
obj = a()
obj.a(obj2)