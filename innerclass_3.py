# defining obj of inner class outside main class

class student:
 
 def a(self):
  print("hi")
 
 class b:
  def hello(self):
   print("hello")

s1 = student()
obj = s1.b()
obj.hello()   