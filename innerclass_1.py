class student:
 
 def a(self):
  print("hi")
  self.obj = self.b()
  self.obj.hello()
 
 class b:
  def hello(self):
   print("hello")

s1 = student()
s1.a()   