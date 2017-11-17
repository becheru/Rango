from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {"boldmessage" : "This is a message from Alex Becheru"}
    return render(request, "tango/index.html", context = context_dict)
    #return HttpResponse("""Rango says hey there partner. </br> Link to the <a href="http://localhost:8000/tango/about">about</a> page """)

def about(request):
    context_dict ={"var1": "This is var1", "var2": "This is var 2"}
    return render(request, "tango/about.html", context = context_dict)
    #return HttpResponse("""Rango says this is the about page. </br> Link to the <a href="http://localhost:8000/tango/">main</a> page """)
