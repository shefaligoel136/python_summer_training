from django.shortcuts import render
def home(request):
	return render(request,'temphtml.html') 

def solve1(request):
	val1 = float(request.POST['num1'])
	val2 = float(request.POST['num2'])
	op = request.POST['op']

	if(op=='+'):
		ans = val1+val2
		return render(request,'temphtml.html',{'res':ans})
	elif(op=='-'):
		ans = val1-val2
		return render(request,'temphtml.html',{'res':ans})
	elif(op=='*'):
		ans = val1*val2
		return render(request,'temphtml.html',{'res':ans})
	elif(op=='/'):
		ans = val1/val2
		return render(request,'temphtml.html',{'res':ans})
	else:
		return render(request,'temphtml.html',{'res':'wrong expression'})
 
def solve2(request):
	val = (request.POST['num'])
	s = eval(val)
	return render(request,'temphtml.html',{'res1':s})