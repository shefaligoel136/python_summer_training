n = int(input("enter total number"))
list_even = []
list_odd = []
for x in range(0,n):
 num = int(input("enter number"))
 if num%2==0:
  list_even.append(num)
 else:
  list_odd.append(num)
print("even elements are",list_even)
print("even_sum is",sum(list_even))
print("odd elements are",list_odd)
print("odd_sum is",sum(list_odd))
