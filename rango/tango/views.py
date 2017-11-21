from django.shortcuts import render
from django.http import HttpResponse
from tango.models import Category
from tango.models import Page

def index(request):
    #context_dict = {"boldmessage" : "This is a message from Alex Becheru"}
    #return render(request, "tango/index.html", context = context_dict)
    #return HttpResponse("""Rango says hey there partner. </br> Link to the <a href="http://localhost:8000/tango/about">about</a> page """)
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = { "categories":category_list }
    return render(request, "tango/index.html", context_dict)

def about(request):
    context_dict ={"var1": "This is var1", "var2": "This is var 2"}
    return render(request, "tango/about.html", context = context_dict)
    #return HttpResponse("""Rango says this is the about page. </br> Link to the <a href="http://localhost:8000/tango/">main</a> page """)

def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug = category_name_slug)
        pages = Page.objects.filter(category = category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['pages'] = None
        context_dict['category'] = None
    return render(request, 'tango/category.html', context_dict)
