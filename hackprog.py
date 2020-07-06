s = "this is a string"
s1 = s.split()
print(s1[0],end='')
s1.remove(s1[0])
for x in s1:
 print('',x,sep='-',end='')
 