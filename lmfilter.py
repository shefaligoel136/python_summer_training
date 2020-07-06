def sq(n):
 k = filter(lambda m:m%2==0,n)
 t = lambda(m:m**2,k)
 return t
l = [1,2,3,4,5,6,7,8,9]
l1 = list(map(sq,l))
print(l1)