from django import forms
from .models import *
from django.contrib.auth.models import User


class AddBookmarkForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].label = 'Категория'

    url = forms.URLField(label='Ссылка', required=True)
    description = forms.CharField(label='Описание', required=False)
    aliace = forms.CharField(label='Псевдоним', required=False)

    class Meta:
        model = Bookmark
        fields = ['url', 'description', 'aliace', 'category', ]


class AddCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Название категории'
        self.fields['parent_category'].label = 'Родительская категория'

    class Meta:
        model = Category
        fields = ['name', 'parent_category', ]


class UpdateBookmarkForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['url'].label = 'Адрес'
        self.fields['description'].label = 'Описание'
        self.fields['aliace'].label = 'Псевдоним'
        self.fields['category'].label = 'Категория'

    class Meta:
        model = Bookmark
        fields = ['url', 'description', 'aliace', 'category', ]

        widgets = {
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 3, 'class': 'bookmark-description'}),
        }
