import base64

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import (get_list_or_404, get_object_or_404, redirect,
                              render)

from short_url_app.forms import UrlForm
from short_url_app.models import Url

User = get_user_model()


def get_short_url(url):
    ''' The function gives a slug for short url.'''

    slug = ascii(base64.b64encode(url.encode()))
    return slug[-7:-1]


@login_required()
def generate_url(request):
    form = UrlForm(
        request.POST
    )

    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.slug = str(get_short_url(instance.url))
        instance.short_url = settings.DOMAIN + instance.slug
        instance.save()
        context = {
            'form': form,
            'short_url': instance.short_url
        }
        return render(request, 'url/create_url.html', context)

    url = request.POST.get('url')
    if url:
        get_obj = get_object_or_404(url=url)
        context = {
            'form': form,
            'short_url': get_obj.short_url
        }
        return render(request, 'url/create_url.html', context)

    context = {
        'form': form,
    }
    return render(request, 'url/create_url.html', context)


@login_required()
def get_list_url(request):
    user = request.user
    list_url = get_list_or_404(Url, user=user)
    template = 'url/url_list.html'
    context = {
        'list_url': list_url,
    }
    return render(request, template, context)


@login_required()
def redirect_url(request, slug):
    url = get_object_or_404(Url, slug=slug)
    origin_url = url.url
    return redirect(origin_url, permanent=True)


def index(request):
    template = 'base.html'
    return render(request, template)
