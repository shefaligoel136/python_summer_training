from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("hello World! you're at the poll index")
