from django.forms import ModelForm
from .models import Task
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','deadline','do_date','start_time','end_time']