from django.forms import ModelForm
from django import forms
from .models import Task
class TaskForm(ModelForm):
    deadline = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    do_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    start_time = forms.TimeField(widget=forms.TextInput(attrs={'type':'time'}))
    end_time = forms.TimeField(widget=forms.TextInput(attrs={'type':'time'}))
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