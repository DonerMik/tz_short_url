from django.forms import ModelForm

from short_url_app.models import Url


class UrlForm(ModelForm):
    class Meta:
        model = Url
        fields = ('url',)
