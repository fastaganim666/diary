from django import forms
from .models import *


class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass


class DateInput(forms.DateInput):
    input_type = 'date'


class AddTaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = TaskDay
        fields = ['name', 'date', ]

        widgets = {
            'date': DateInput()
        }
