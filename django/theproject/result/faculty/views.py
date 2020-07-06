from django.shortcuts import render,redirect
from .models import faculty_login
from student.models import students
# Create your views here.
def faculty(request):
	if request.session.get('user'):
		return redirect('home')
	else:	
		return render(request,'faculty.html')
	
def flogin(request):
	username = request.POST['fuser']
	password = request.POST['fpass']
	
	res = faculty_login.objects.filter(fuser=username,fpass=password)
	
	if len(res)==1:
		request.session['user']=res[0].fuser
		return redirect('home')
	else:
		return render(request,'faculty.html',{'error':'Username or Password Incorrect!!!'})

def home(request):
	if request.session.get('user'):
		return render(request,'home.html')
	else:
		return redirect('/faculty/')

def logout(request):
	del request.session['user']
	return redirect('/faculty/')
	
def account(request):
	if request.session.get('user'):
		return render(request,'account.html')
	else:
		return redirect('/faculty/')
		
def create_account(request):
	rollnum = request.POST['rollnum']
	name = request.POST['sname']
	password = request.POST['spass']
	
	res = students.objects.filter(rollnum=rollnum)
	
	if len(res)>0:
		return render(request,'account.html',{'error':'Student already exists with given roll number.'})
	else:
		q = students(rollnum=rollnum, sname=name, spass=password)
		q.save()
		return render(request,'account.html',{'error':'Account created successfully.'})
	
def marks(request):
	res = students.objects.all()
	return render(request,'marks.html',{'res':res})

def updated_marks(request):
	marks = request.POST.getlist('nums')
	
	res = students.objects.all()
	
	ln = len(res)+1
	
	for i,j in zip(range(1,ln),marks):
		upd = students.objects.get(id=i)
		upd.marks=j
		upd.save()
	
	res = students.objects.all()
	return render(request,'updated_marks.html',{'res':res})
	
def chk_marks(request):
	res = students.objects.all()
	return render(request,'chk_marks.html',{'res':res})