from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    # Title of the task:
    title = models.CharField(max_length=100)
    # Short description:
    description = models.TextField(blank=True)
    # When the task was created:
    created = models.DateField(auto_now_add=True)
    # The time you need to completed the task
    time_req = models.CharField(max_length=100,null=True,blank=True)
    # Task has been completed or not:
    completed = models.BooleanField(null=True,blank=True)
    # Date on which you completed the task:
    completed_date = models.DateTimeField(null=True,blank=True)
    
    # The user whom created the task:
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
# -----------Viewing the title in DjangoAdmin-------------
    def __str__(self):
        return self.title