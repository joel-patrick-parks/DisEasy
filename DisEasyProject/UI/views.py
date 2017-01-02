from django.shortcuts import render

def home(request):
    return render(request, 'UI/index.html')

def form(request):
    return render(request, 'UI/form.html')

def result(request):
    return render(request, 'UI/result.html')
