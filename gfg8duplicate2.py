s = "Geeekksforgeeekks"
c = "p"
z=0
s1=""
for x in range(len(s)):
 print('x =', x)
 for i in range(x+1,len(s)):
  print('i=', i)
  if s[x]==s[i]:
   z=z+1
   print('z = ',z)
   x = x+z
   print('x =', x)
   if(z==1):
    s1 = s1+c
    print(s1)
    break
  else:
   s1 = s1+s[x]
   print(s1)
   z = 0
   break
print(s1)