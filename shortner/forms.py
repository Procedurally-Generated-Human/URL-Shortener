from django import forms
from .models import UrlLink

import hashlib, base64

class UrlForm(forms.ModelForm):

    url = forms.CharField(label='Your URL', max_length=1000)

    def generate_short_url(self, text):
        text_utf8 = text.encode('utf8')
        md5 = hashlib.md5(text_utf8).digest()
        b64 = base64.b64encode(md5)
        result = b64.decode()[:10]
        return result

    class Meta:
        model = UrlLink
        fields = ['url']