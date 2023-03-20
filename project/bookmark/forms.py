from django import forms
from .models import *


class AddBookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ['url', 'description', 'aliace', 'category', ]