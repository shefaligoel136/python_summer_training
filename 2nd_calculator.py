print("enter your expression")
n1 = int(input("number"))
op = input("operator")
n2 = int(input("number"))
if op=='+':
 c = n1+n2
 print(c)
elif op=='-':
 c = n1-n2
 print(c)
elif op=='*':
 c = n1*n2
 print(c)
elif op=='/':
 c = n1/n2
 print(c)
else:
 print("Invalid Expression")