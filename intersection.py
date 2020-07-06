a1=[1,2,3,4,1,2]
a2=[2,4,6,8,4]
a1 = set(a1)
a2 = set(a2)
a3 = []
for x in a1:
 if x in a2:
  a3.append(x)
print(a3)
 
