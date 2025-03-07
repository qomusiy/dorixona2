from django import forms
from .models import Pills


class PillForm(forms.ModelForm):
    class Meta:
        model = Pills
        fields = '__all__'