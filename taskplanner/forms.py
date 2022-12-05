from django.forms import ModelForm
from .models import Task
class taskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','time_req','deadline']