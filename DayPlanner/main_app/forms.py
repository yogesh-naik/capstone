from django import forms
from django.forms import ModelForm
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name','tag','user']
        # exclude = ['user']
        
        def __init__(self, *args, **kwargs):
            super(TaskForm, self).__init__(*args, **kwargs)
            
class TaskEditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name','tag']
        
        def __init__(self, *args, **kwargs):
            super(TaskEditForm, self).__init__(*args, **kwargs)
            self.fields['name','tag'].required = False
        