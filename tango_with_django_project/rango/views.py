from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World! <br /> <a href='/rango/about'>About</a>")

def about(request):
    return HttpResponse("Rango about page <a href='/rango/'>Home</a>")
