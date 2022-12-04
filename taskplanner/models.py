from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    time_req = models.TimeField(null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
# -----------Viewing the title in DjangoAdmin-------------
    def __str__(self):
        return self.title