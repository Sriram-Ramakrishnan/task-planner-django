from django.forms import ModelForm
from .models import Task
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','deadline','do_date','start_time','end_time']
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            data = {
                "class": "form-control"
            }
            self.fields[str(field)].widget.attrs.update(
                data
            )