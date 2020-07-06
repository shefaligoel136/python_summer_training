def suming(*a):
 s = 0
 for i in a:
  s = s+i
 print(s)

def mul_div(a=3,b=78):
 return (a*b,a//b)

def divide(k):
 s = []
 l = [3,6,9,12,15]
 f = (lambda num,d:num/d)
 for i in l:
  div = f(i,k)
  s.append(div)
 print(s)
  
def gl():
 global a
 a = "in function global"
 print(a)
 
a = "original global" 
print("enter 1 for suming up numbers")
print("enter 2 fo multipling and divide munbers")
print("enter 3 for divding number by a particular number")
print("enter 4 for global and local explanation")
c = int(input(""))

if c==1:
 suming(1,2,3,4,5)
elif c==2:
 m,d= mul_div(298,76)
 print(m,d)
elif c==3:
 n = int(input("enter number "))
 divide(n)
else:
 print(a)
 gl()
 print(a)
 a = "new global"
 print(a)
 
