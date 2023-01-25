from django import forms
from django.forms.widgets import NumberInput
import re
from django.core import validators


class Pas(forms.Form):
    sNo = forms.IntegerField(label="seat Number")
    name = forms.CharField(max_length=70, label='name')
    mailId = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    photo = forms.ImageField(label='Photo')
    dot = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    persons = forms.IntegerField()
    cost = forms.IntegerField()

