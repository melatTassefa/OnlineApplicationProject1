from django.shortcuts import render

# Create your views here.

def contact(request):
    return render(request, 'contact.html')


def aboutus(request):
    return render(request, 'aboutus.html')

def login(request):
    return render(request, 'login.html')


def registration(request):
    return render(request, 'registration.html')

def college_search(request):
    return render(request, 'college_search.html')