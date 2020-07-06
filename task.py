class task:
	def __init__(self,a):
		self.a = a
 
	def repeat_unique(self):
		k1 = []
		k2 = []
		count = 0
		for x in self.a:
			count = 0
			if x not in k1:
				for y in range(0,len(self.a)):
					if x==self.a[y]:
						count = count+1
				if count>1:
					print("{}   is repeated {}   times ".format(x,count))
					k1.append(x)
				else:
					"""print("{}    is unique".format(x))"""
					k2.append(x)
			else:
				continue
		return k2
	
	def show_unique(self,l1):
		for x in l1:
			print("{}    is unique".format(x))
    
l = [] 
n = int(input("Enter max no. in the list"))
print("Enter the Numbers")
for x in range(n):
 m = int(input())
 l.append(m)

t = task(l)
l1= t.repeat_unique()
t.show_unique(l1)


# 1 2 4 3 2 5 4 3