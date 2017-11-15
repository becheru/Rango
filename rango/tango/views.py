from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("""Rango says hey there partner. </br> Link to the <a href="http://localhost:8000/tango/about">about</a> page """)

def about(request):
    return HttpResponse("""Rango says this is the about page. </br> Link to the <a href="http://localhost:8000/tango/">main</a> page """)
