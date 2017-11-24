from django.shortcuts import render
from django.http import HttpResponse
from tango.models import Category
from tango.models import Page
from tango.forms import CategoryForm
from tango.forms import PageForm

def index(request):
    #context_dict = {"boldmessage" : "This is a message from Alex Becheru"}
    #return render(request, "tango/index.html", context = context_dict)
    #return HttpResponse("""Rango says hey there partner. </br> Link to the <a href="http://localhost:8000/tango/about">about</a> page """)
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by("-views")[:5]
    context_dict = { "categories":category_list,"most_visited_pages":page_list}
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

def add_category(request):
    form = CategoryForm
    print("Entered category view")
    print(request.method)
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            cat = form.save(commit = True)
            print(cat, cat.slug, "Category Added")
            return index(request)
        else:
            print(form.errors)
    return render(request, 'tango/add_category.html', {'form':form})

def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug = category_name_slug)
    except Category.DoesNotExist:
        category = None

    form = PageForm()
    if request.method == "POST":
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit = False)
                page.category = category
                page.views = 0
                page.save()
                return show_category(request, category_name_slug)
        else:
            print(form.errors)
    context_dict = {'form':form, 'category':category}
    return render(request, 'tango/add_page.html', context_dict)
