#  Exception Handling
""" 1) Compile Time
    2) Logicacl
	3) Run Time """
	
a = 5
b = [0,7,5,"str"]
for x in range(len(b)):
 try:
  print(a/b[x+1])
  try:
   assert a==b[x+1]
   print("found", a)
  except AssertionError as e:
   pass
 except TypeError:
  print("Type Error - div by string")
 
 except ZeroDivisionError:
  print("ZeroDivisionError - div by 0")
 
 except IndexError:
  print("Index not Found")
 
 except Exception as e:
  print("NOTE:", e)
 
 
 finally:
  print("Done")

