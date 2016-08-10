from django import forms
from models import File
from django.forms import ModelForm


class UploadFileForm(ModelForm):

    class Meta:
        model = File
        fields = ('filename_text', 'description_text','file')