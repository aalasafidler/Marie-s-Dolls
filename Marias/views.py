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

def dolls_collection(request):
    return render(request, 'dolls/dolls_collection.html')

def success(request):
    return render(request, 'success.html')

def caoilin(request):
    return render(request, 'dolls/caoilin.html')

def tiffany(request):
    return render(request, 'dolls/tiffany.html')

def petal(request):
    return render(request, 'dolls/petal.html')

def jenny(request):
    return render(request, 'dolls/jenny.html')

def poppy(request):
    return render(request, 'dolls/poppy.html')

def clodagh(request):
    return render(request, 'dolls/clodagh.html')

def daithi(request):
    return render(request, 'dolls/daithi.html')

def peaches(request):
    return render(request, 'animals/peaches.html')

def product_template(request):
    return render(request, 'product_template.html')
