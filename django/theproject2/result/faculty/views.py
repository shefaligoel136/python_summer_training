from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import faculty_login
from student.models import *

def faculty(request):    
	if request.session.get('user'):
		return redirect('fhome')
	else:
		return render(request,'faculty.html')

def flogin(request):
	fname = request.POST['fname']
	fpass = request.POST['fpass']
	fcheck = faculty_login.objects.filter(fname=fname,fpass=fpass)
	# the first fname in .filter is the value from the user and 
	# second fname is the variable in which it is stored
	
	if len(fcheck)==1:
		request.session['user']=fcheck[0].fname
		return redirect('fhome')
	else:
		return render(request,'faculty.html',{'error':'username or password not correct!'})
		
		
def fhome(request):
	if request.session.get('user'):
		return render(request,'fhome.html')
	else:
		return redirect('faculty')

def flogout(request):
	del request.session['user']
	return redirect('faculty')
	
def faccount(request):
	if request.session.get('user'):
		return render(request,'faccount.html')
	else:
		return redirect('faculty')
	
def create_account(request):
	name = request.POST["sname"]
	password = request.POST["spassword"]
	rollnum = request.POST["srollnum"]
	
	rcheck = students.objects.filter(srollnum = rollnum)
	if len(rcheck)>0:
		return render(request,'faccount.html',{'error': 'Student already exists with given rollnumber.'})
	else:
		q = students(srollnum=rollnum,sname=name,spassword=password)
		q.save()
		return render(request,'faccount.html',{'error':'Account created Successfully!'})
		
def marks(request):
	res = students.objects.all()
	return render(request,'marks.html',{'res':res})
	
def update_marks(request):
	marks = request.POST.getlist('nums')
	return render(request,'marks.html',{'marks':marks})
	
	