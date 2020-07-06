def add():
 x = 1
 while x<=10:
  yield x*x
  x+=1
  
value = add()
for k in add():
 print(value.__next__()) 