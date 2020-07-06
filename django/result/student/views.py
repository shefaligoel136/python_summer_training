from django.shortcuts import render,redirect
from .models import students
# Create your views here.
def student(request):
	if request.session.get('rollnum'):
		return redirect('shome')
	else:	
		return render(request,'student.html')
	
def slogin(request):
	rollnum = request.POST['rollnum']
	password = request.POST['spass']
	
	res = students.objects.filter(rollnum=rollnum,spass=password)
	
	if len(res)==1:
		request.session['rollnum']=res[0].rollnum
		return redirect('shome')
	else:
		return render(request,'student.html',{'error':'Roll Number or Password Incorrect!!!'})

def shome(request):
	if request.session.get('rollnum'):
		return render(request,'shome.html')
	else:
		return redirect('/student/')

def slogout(request):
	del request.session['rollnum']
	return redirect('/student/')

def s_chk_marks(request):
	res = students.objects.all()
	return render(request,'s_chk_marks.html',{'res':res})