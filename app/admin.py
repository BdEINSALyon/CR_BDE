from django.contrib import admin

from .models import *

# Register your models here.
@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = '__str__', 'date', 'type',
    list_display_links = '__str__',
    search_fields = 'date',
    list_filter = 'type', 'year'


@admin.register(Type, Year)
class Admin(admin.ModelAdmin):
    pass
