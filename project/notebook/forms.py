from django import forms
from tinymce.widgets import TinyMCE
from .models import *


# class AddNoteForms(forms.ModelForm):
#     content = forms.CharField(widget=TinyMCE())

class AddNoteForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE())
    class Meta:
        model = Note
        fields = ['title', 'content', 'category']
        widgets = {
            'title': forms.TextInput(),
        }
