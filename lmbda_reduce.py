import functools 
num=[1,2,3,4,5,6,32,21] 
r = functools.reduce(filter(lambda a,b : a+b,num))
print(r)