""" Forms for the app. """
from django import forms
from django.forms.fields import CharField
from django.forms.widgets import Input

# class SearchForm(forms.Form):
#     search = forms.CharField()

class NewEntry(forms.Form):
    title = forms.CharField(max_length=80)
    # content = forms.Textarea()
    content = forms.CharField(widget=forms.Textarea)
    # foo = forms.TextInput()
