from django import forms
from .models import UrlLink

import random

class UrlForm(forms.ModelForm):

    url = forms.CharField(label='Your URL', max_length=1000)

    def generate_short_url(self):
        short_url = random.randint(1,20)
        return short_url

    class Meta:
        model = UrlLink
        fields = ['url']