class b:
 def k(self):
  print("this is k func")
  
class a:
 def a(self,obj2):
  obj2.k()

obj2 = b()
obj = a()
obj.a(obj2)