from django import forms
from .models import Websites

WEBSITES = [(site.spider_name , site.website_title) for site in Websites.objects.all().filter(working=True)]

class SearchForm(forms.Form):
    query = forms.CharField(max_length=45, required=True)
    websites = forms.MultipleChoiceField(choices=WEBSITES, widget=forms.CheckboxSelectMultiple(attrs={"checked":True}), label="Available Websites:", required=True)
