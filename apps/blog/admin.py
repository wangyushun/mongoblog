from django.contrib import admin
from .models import Category, Blog

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    list_editable = ('name',)



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'add_time')
    list_display_links = ('id', 'title')

    list_filter = ('category', 'add_time')
    search_fields = ['title', 'content']
    list_editable = ('author',)



