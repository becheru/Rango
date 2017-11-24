from django.contrib import admin
from tango.models import Category, Page
from tango.models import UserProfile

class PageAdmin(admin.ModelAdmin):
    list_display = ["title", "url", "category"]

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(UserProfile)

# Register your models here.
