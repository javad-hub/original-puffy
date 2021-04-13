from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    # return HttpResponse('Hello this is puffy network')
    return render(request , 'About.html')

def home(request):
    # return HttpResponse('Home')
    return render(request , 'Home.html')
