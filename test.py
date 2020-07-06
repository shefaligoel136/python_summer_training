def fun(s):
 l = len(s)
 t,d = 0,0
 for x in s:
  if x=='@':
   t = t+1
  elif x =='.':
   d = d+1
 if(t==1 and d==1 	):
  e,u = s.split('@')
  w,c = u.split('.')
  count = 0
  if(len(e)!=0 and len(w)!=0 and len(c)!=0):
   for x in e:
    if x.isalnum() or x=='-' or x=='_':
        count = count+1
   for x in w:
     if x.isalnum():
      count = count+1
   if len(c)<=3:
     count = count+len(c)
   if count == l-2:
    return s
a = ["itsme@gmail","@something","@something.com","@something.co1","sone.com"]
k = list(map(fun,a))
print(k)