from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'landing/index.html', {'title' : 'KryptSec Society'})

def about(request):
    return render(request, 'landing/about.html', {'title' : 'about us' })