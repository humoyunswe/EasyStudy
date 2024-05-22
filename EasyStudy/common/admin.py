from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title',)
