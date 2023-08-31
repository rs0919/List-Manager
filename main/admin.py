from django.contrib import admin
from .models import ToDoList, Item

# Register your models here.

admin.site.register(ToDoList) # give admin page access to ToDoList database
admin.site.register(Item)