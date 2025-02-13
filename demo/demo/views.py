from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the MySite!")

def about(request):
    return HttpResponse("Welcome to About page")

def contact(request):
    return HttpResponse("Welcome to Contact page")