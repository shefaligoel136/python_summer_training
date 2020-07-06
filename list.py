Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #lists
>>> n=[1,2,3,4]
>>> n1=['a','s','d','f','g']
>>> n2=['q',7,'w',6,'e',5]
>>> mix[n,n1,n2]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    mix[n,n1,n2]
NameError: name 'mix' is not defined
>>> mix= [n,n1,n2]
>>> mix
[[1, 2, 3, 4], ['a', 's', 'd', 'f', 'g'], ['q', 7, 'w', 6, 'e', 5]]
>>> mix[2][3]
6
>>> n.append(11)
>>> 
>>> n
[1, 2, 3, 4, 11]
>>> n.insert(0,55)
>>> n
[55, 1, 2, 3, 4, 11]
>>> n.index(9,11)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    n.index(9,11)
ValueError: 9 is not in list
>>> n.remove(55)
>>> n
[1, 2, 3, 4, 11]
>>> n.pop(3)
4
>>> n
[1, 2, 3, 11]
>>> n.pop()
11
>>> n
[1, 2, 3]
>>> del n[0:2]
>>> n
[3]
>>> del n
>>> n
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    n
NameError: name 'n' is not defined
>>> n=[1,2,3,4,5]
>>> sum(n)
15
>>> max(n)
5
>>> min(n)
1
>>> sort(n)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    sort(n)
NameError: name 'sort' is not defined
>>> n.sort()
>>> n
[1, 2, 3, 4, 5]
>>> n.sort(reverse = True)
>>> n
[5, 4, 3, 2, 1]
>>> n.extend([8,99])
>>> n
[5, 4, 3, 2, 1, 8, 99]
>>> print(len(n1))
5
>>> n3= n.copy()
>>> print(n3)
[5, 4, 3, 2, 1, 8, 99]
>>> n3.reverse()
>>> n3
[99, 8, 1, 2, 3, 4, 5]
>>> k=  n.count(8)
>>> k
1
>>> n is n3
False
>>> n is not n3
True
>>> n3.reverse()
>>> n is n3
False
>>> n==n3
True
>>> 
