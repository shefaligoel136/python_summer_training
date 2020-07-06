class student:
 school = "vsics"
  
 @classmethod     #decorators to access class instances
 def get_school(cls):    #it is standard to use cls with classmethod
  print(cls.school)
  
s1 = student()
student.get_school()