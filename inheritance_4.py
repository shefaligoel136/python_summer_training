# using super

class a:
 def __init__(self):
  print("initof A")
 
 def feature1(self):
  print("feature 1 is working")
  
 def feature2(self):
  print("feature 2 is working")
  
class b(a):
 def __init__(self):
  super().__init__()
  print("initof B")
  
 def feature3(self):
  print("feature 3 is working")
  
 def feature4(self):
  print("feature 4 is working")
  
k = b()
k.feature1()