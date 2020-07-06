def f(n):
 m = 1
 while n>0:
  m = m*n
  n = n-1
 return m

l = [5,6,7]
l1 = list(map(f,l))
print(l1)
l2 = []
a = list((lambda num:num*2))
for i in l:
 a(i)
 """l2.append(m2)
print(l2)"""
 
print(a)