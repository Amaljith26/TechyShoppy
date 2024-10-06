from django.shortcuts import render

# Create your views here.

def products(request):
    return render(request,'mens.html')

def products2(request):
    return render(request,'womens.html')

def products3(request):
    return render(request,'kids.html')

