from django.contrib import admin

# Register your models here.
from .models import Category, Course, Contact

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Contact)