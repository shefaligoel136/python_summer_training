from django.shortcuts import render

def home(request):
	return render(request,'pyhome.html',{'name':'Shefali'})
	
def add(request):
	val1 = int(request.POST['num1'])
	val2 = int(request.POST['num2'])
	op = request.POST['op']
	
	if(op=='+'):
		ans = val1+val2
		return render(request,'pyhome.html',{'res':ans})
	elif(op=='-'):
		ans = val1-val2
		return render(request,'pyhome.html',{'res':ans})
	elif(op=='*'):
		ans = val1*val2
		return render(request,'pyhome.html',{'res':ans})
	elif(op=='/'):
		ans = val1/val2
		return render(request,'pyhome.html',{'res':ans})
	else:
		return render(request,'pyhome.html',{'res':'wrong expression'})