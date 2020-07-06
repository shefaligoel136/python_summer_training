s = "Geeksforgeeks"
c = "e"
z=0
s1=""
for x in range(len(s)):
 if s[x]==c:
  z = z+1
  if z==1:
   s1 = s1+c
 else:
  s1 = s1+s[x]
  z = 0
print(s1)