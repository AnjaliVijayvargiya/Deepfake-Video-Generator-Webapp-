from django import forms
from .models import video
from .models import video2

class videoForm(forms.ModelForm):
    class Meta:
        model = video
        fields=("video1","video2",)

class videoForm2(forms.ModelForm):
    class Meta:
        model = video2
        fields=("image","video3",)