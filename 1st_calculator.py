n = list(input("enter your expression to be calculated"))
l = len(n)
s = int(n[0])
k = 2
for x in range(1,l,2):
  if n[x]=='+':
   s = s+int(n[k])
   k=k+2
  elif n[x]=='*':
   s = s*int(n[k])
   k=k+2
  elif n[x]=='/':
   s = s/int(n[k])
   k=k+2
  elif n[x]=='-':
   s = s-int(n[k])
   k=k+2
  else:
   print("not found")
print(s)