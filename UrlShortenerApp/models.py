from django.db import models

class Url(models.Model):
    link_url = models.URLField(max_length=5000, null=False, blank=False)
    uuid = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.link_url} - {self.uuid}'
