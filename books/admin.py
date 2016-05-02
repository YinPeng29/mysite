#-*- coding:utf-8 -*-
from django.contrib import admin

# Register your models here.
from books.models import Publisher,Author,Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email')
    search_fields = ('first_name','last_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','publisher','publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    fields = ('title','authors','publisher','publication_date')
    filter_horizontal = ('authors',)
    filter_vertical = ('authors',)    #只适用于多对多字段
    raw_id_fields = ('publisher',)

admin.site.register(Publisher)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)