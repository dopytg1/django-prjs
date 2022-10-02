from django.contrib import admin
from .models import *
# Register your models here.


class DressAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'photo', 'text')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text')
    list_editable = ('price', )
    prepopulated_fields = {'slug': ('title', )}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', )
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Dress, DressAdmin)
admin.site.register(Categories, CategoryAdmin)