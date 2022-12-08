from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Task(models.Model):
    # Title of the task:
    title = models.CharField(max_length=100)
    # Short description:
    description = models.TextField(blank=True)
    # When the task was created:
    created = models.DateField(auto_now_add=True)
    start_time = models.TimeField(null=True,blank=True)
    end_time = models.TimeField(null=True,blank=True)
    # The time you need to completed the task
    deadline = models.DateField(null=True,default=now()) 
    do_date = models.DateField(null=True,blank=True)
    # Task has been completed or not:
    completed = models.BooleanField(null=True,blank=True)
    # Date on which you completed the task:
    completed_date = models.DateTimeField(null=True,blank=True)
    
    # The user whom created the task:
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
# -----------Viewing the title in DjangoAdmin-------------
    def __str__(self):
        return self.title