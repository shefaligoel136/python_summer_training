from django.shortcuts import render
from django.http import HttpResponse
def home_view(request,*args,**kwargs):
	print(args,kwargs)
	print(request.user)
	my_context = {
		"my_text": "about me",
		"this_is_true": True,
		"my_number": 123,
		"my_list": [123,232,12334,'abc']
    }
	"""for item in [122,12321]:
		my_context['item1'] = item"""
	return render(request,"home.html",my_context) 
