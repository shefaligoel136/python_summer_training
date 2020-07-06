import itertools
def isPrime(n):
 count = 0
 for x in range(1,n+1):
  if(n%x)==0:
   count = count+1
 if(count==2):
  return n
 else:
  pass
r = int(input("enter the constraint last no"))
lis = []
for x in range(1,r):
 count = 0
 for n in range(1,x+1):
  if(x%n)==0:
   count = count+1
 if(count==2):
  lis.append(n)
#print(lis)
l = (list(itertools.accumulate(lis,lambda x,y : x+y))) 
#print(l)
k = list(map(isPrime,l))
#print(k)
c = 0
for x in k:
 try:
  if(type(x)==type(int()) and x>2 and x<r):
   c = c+1
   #print(x)
 except Exception:
  pass
print(c)