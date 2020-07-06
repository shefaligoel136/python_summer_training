class hello:
 def hi(self): """we are using self because object is passed as a parameter by default when the object calles a function in class
                  ----- hence we use self in function definition(it is a standard) but we can use any other variable"""
  print("hello")
obj = hello()  #object created
obj.hi() #object calling the function 