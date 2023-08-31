from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# models.Model is like the base class for data models.

class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    # ^ Foreign key is used for user-def type
    # ^ on_delete will delete items if the todolist is deleted
   
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text