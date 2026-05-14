from django import forms
from .models import UserFile


class FileForm(forms.ModelForm):
    class Meta:
        model = UserFile
        fields = ['file', 'category']