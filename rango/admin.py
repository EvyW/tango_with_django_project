from django.contrib import admin
from rango.models import Category, Page

# Notes:
# you can customise the Admin interface in a number of ways, check the documentation

# Register your models here:
admin.site.register(Category)
admin.site.register(Page)