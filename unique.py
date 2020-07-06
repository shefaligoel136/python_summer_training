a = [9,4,7,5,6]
c = 0

for i in a:
 c = c + a.count(i)

if c == (len(a)):
 print("unique")
else:
 print("not unique")
"""  ---  or
a = [9,4,7,5,6]
if (len(a)==len(set(a))):
 print("unique")
else:
 print("not unique") --- """