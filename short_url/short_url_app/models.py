from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Url(models.Model):
    url = models.URLField('ВведитеURL:',
                          unique=True
                          )
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='list_url'
                             )
    slug = models.SlugField(max_length=6,
                            unique=True
                            )
    short_url = models.URLField('Short URL:', blank=True,
                                null=True,
                                unique=True
                         )
