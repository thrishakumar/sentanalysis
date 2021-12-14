from django.db import models


class Link(models.Model):
    objects = None
    link = models.URLField(max_length=200)

    def __str__(self) -> object:
        return self.link
