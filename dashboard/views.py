from django.shortcuts import render

# Create your views here.

def dashboard(request):
	return render(request,'dashboard/index.html')

def text_summary(request):
	return render(request,'dashboard/summary.html')