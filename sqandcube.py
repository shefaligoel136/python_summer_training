def square():
 t = int(input("enter the total numbers you want"))
 print("enter the numbers")
 num = []
 l=[]
 for x in range(t):
  k = int(input(""))
  num.append(k)
 for x in num:
  l.append(x**2)
 print(sum(l))
 
def cube():
 t = int(input("enter the total numbers you want"))
 print("enter the numbers")
 num=[]
 l=[]
 for x in range(t):
  k = int(input(""))
  num.append(k)
 for x in num:
  l.append(x**3)
 print(sum(l))
 
print("press 1 to get the sum of square of n natural numbers")
print("press 2 to get the sum of cube of n natural number")
choice = int(input(""))

if choice == 1:
 square()
elif choice == 2:
 cube()
else:
 print("Wrong Choice!")
 

 

