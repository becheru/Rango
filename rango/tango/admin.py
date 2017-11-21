from django.contrib import admin
from tango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ["title", "url", "category"]

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)

# Register your models here.
