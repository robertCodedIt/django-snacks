from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return render(request,'home/about.html')
def home(request):
    return render(request,'home/home.html')
# Create your views here.
