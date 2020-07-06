from django.shortcuts import render

# Create your views here.
def prouct_detail_view(request):
	return render(request,'product/detail.html',{})