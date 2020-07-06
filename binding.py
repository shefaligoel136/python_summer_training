class A:
 x = 5
 def a(self):
  self.x = 9
 def b(t):
  t.x = 77
  
obj = A()
obj.a()
print(obj.x)
obj.b()
print(A.x)
print(obj.x)