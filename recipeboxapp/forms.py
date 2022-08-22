from django import forms
from recipeboxapp.models import Author


class Recipeform(forms.Form):
    title = forms.CharField(max_length=100)
    body = forms.CharField(widget=forms.Textarea)
    author = forms.ChoiceField(queryset=Author.objects.all())


class Authorform(forms.Form):
    ...
