# multiple inheritance - super
""" constructor behaviour in multiple inheritance -- Method Resolution Order(MRO) """

class a:

 def __init__(self):
  super().__init__()
  print("initof A")
  
 def feature1(self):
  print("feature 1 is working")
  
 def feature2(self):
  print("feature 2 is working")
  
class b:
 
 def __init__(self):
  super().__init__()
  print("initof B")
  
 def feature3(self):
  print("feature 3 is working")
  
 def feature4(self):
  print("feature 4 is working")
  
class c(a,b):

 def __init__(self):
  super().__init__()
  print("initof C")
  
 def feature5(self):
  print("feature 5 is working")


obj1 = c()
obj1.feature1()