from django.db import models
from django.utils import timezone

today = timezone.now()


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    date = models.DateField(default=today)

    def __str__(self):
        return self.title 