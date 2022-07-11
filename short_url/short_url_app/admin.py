from django.contrib import admin
from short_url_app.models import Url


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ('url', 'user', 'slug', 'short_url')
