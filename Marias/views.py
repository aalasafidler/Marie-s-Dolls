from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def store(request):
    return render(request, 'store.html')

def products(request):
    return render(request, 'products.html')