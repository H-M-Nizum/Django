from django.shortcuts import render
from django.template.context_processors import request

# Create your views here.
def homeView(request):
    print("Inside Home View ===================== ")
    return render(request, "myapp/home.html")


def aboutView(request):
    return render(request, 'myapp/about.html')

def servicesView(request):
    return render(request, 'myapp/services.html')

def contactView(request):
    return render(request, 'myapp/contact.html')