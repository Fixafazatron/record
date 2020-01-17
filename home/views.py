from django.shortcuts import render

def index(request):
    return render(request, 'home/main.html')

def about(request):
    return render(request, 'home/about.html')

def category(request):
    return render(request, 'home/category.html')

