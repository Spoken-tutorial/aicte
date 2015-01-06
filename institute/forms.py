from django import forms
from django.forms import ModelForm
from institute.models import *

class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
