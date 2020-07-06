str1 = "I km zogicazzy izz"
s = ''
for i in str1:
 if i == 'k':
  s = s+'a'
 elif i == 'z':
  s = s+'l'
 else:
  s = s+i
print(s)
