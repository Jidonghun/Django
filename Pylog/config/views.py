from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def css_test(request):
    return render(request, 'css_test.html')