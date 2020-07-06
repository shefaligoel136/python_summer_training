from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import students

def student(request):
	if request.session.get('user'):
		return redirect('shome')
	else:
		return render(request,'student.html')

def slogin(request):
	name = request.POST['sname']
	password = request.POST['spassword']
	scheck = students.objects.filter(sname=name,spassword=password)
	
	if len(scheck)==1:
		request.session['user']=scheck[0].sname
		return redirect('shome')
	else:
		return render(request,'student.html',{'error':'username or password not correct!'})
		
		
def shome(request):
	if request.session.get('user'):
		return render(request,'shome.html')
	else:
		return redirect('student')

def slogout(request):
	del request.session['user']
	return redirect('student')