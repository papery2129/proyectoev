from django import forms
from django.core import validators
from app.models import comentarios


class FormUser(forms.ModelForm):
    class Meta:
        model = comentarios
        fields = '__all__'
