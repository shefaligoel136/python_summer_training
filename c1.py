t = int(input())
for i in range(t):
	p = input()
	s = input()
	for x in range(len(p)):
		for y in range(len(s)):
			if(p[x]==s[y]):
				print(s[y], end="")
	print('')