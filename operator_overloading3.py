class Test:
 def __init__(self,a1,a2,a3):
  self.a1 = a1
  self.a2 = a2
  self.a3 = a3
  
 def __add__(n1,n2):
  m1 = n1.a1+n2.a1
  m2 = n1.a2+n2.a2
  m3 = n1.a3+n2.a3
  m = Test(m1,m2,m3)
  return m
 def __mul__(n1,n2):
  m1 = n1.a1*n2.a1
  m2 = n1.a2*n2.a2
  m3 = n1.a3*n2.a3
  m = Test(m1,m2,m3)
  return m
  
nn1 = Test(2,3,4)
nn2 = Test(12,13,14)
nn3 = Test(22,23,24)
nn4 = nn2+nn3*nn1
print(nn4.a1 , nn4.a2 , nn4.a3)