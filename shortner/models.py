from django.db import models

class UrlLink(models.Model):

    original_url = models.CharField(max_length = 1000)
    short_url = models.CharField(max_length = 100)

    def __str__(self):
        return self.short_url

