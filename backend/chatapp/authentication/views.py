from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'index.html')

def register(request):
    pass