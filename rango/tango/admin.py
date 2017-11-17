from django.contrib import admin
from tango.models import Category, Page

admin.site.register(Category)


class PageAdmin(admin.ModelAdmin):
    list_display = ["title", "url", "category"]

admin.site.register(Page, PageAdmin)

# Register your models here.
