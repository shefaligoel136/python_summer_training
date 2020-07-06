#using object of inner class outside main class
class student:
 
 def a(self):
  print("hi")
  self.obj = self.b()
 
 class b:
  def hello(self):
   print("hello")

s1 = student()
s1.a() 
s1.obj.hello()  