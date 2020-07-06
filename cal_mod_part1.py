import cal_mod
print("press 1 to add")
print("press 2 to sub")
print("press 3 to div")
print("press 4 to mul")

n = int(input("enter your choice"))

if n==1:
 n1 = int(input("enter first number:"))
 n2 = int(input("enter second number"))
 a = cal_mod.add(n1,n2)
 print(a)
 
elif n==2:
 n1 = int(input("enter first number:"))
 n2 = int(input("enter second number"))
 s = cal_mod.sub(n1,n2)
 print(s)
 
elif n==3:
 n1 = int(input("enter first number:"))
 n2 = int(input("enter second number"))
 d = cal_mod.div(n1/n2)
 print(s)
 
elif n==4:
 n1 = int(input("enter first number:"))
 n2 = int(input("enter second number"))
 m = cal_mod.mul(n1,n2)
 print(m)
 
else:
 print("you gave a wrong choice!")