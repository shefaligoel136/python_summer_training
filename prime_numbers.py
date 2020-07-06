def prime_no(n1,n2):
 prime_list = []
 for x in range(n1,n2+1):
  count=0
  for p in range(1,x+1):
   if x%p==0:
    count= count+1
  if count==2:
   prime_list.append(x)
 print("The prime numbers in the range {} to {} are".format(n1,n2),prime_list)
num1,num2 = [int (num1) for num1 in input("give the range ").split()]
prime_no(num1,num2)


  