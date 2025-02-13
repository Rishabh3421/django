from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Welcome to the MySite!")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("Welcome to About page")

def contact(request):
    return HttpResponse("Welcome to Contact page")