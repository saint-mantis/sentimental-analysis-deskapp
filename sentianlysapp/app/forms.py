from django import forms
from django.forms import ClearableFileInput, FileInput
from .models import SmModel

class SmForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
         kwargs.setdefault('label_suffix', '')
         super(SmForm, self).__init__(*args, **kwargs)


    class Meta:
        model = SmModel
        labels = {
            'inputText': 'Enter Text',
            
        }
        fields = ['inputText']