from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base.html')

def home_one(request):
    return render(request, 'home.html')