from django.db import models
from django.utils import timezone


class List(models.Model):
    title = models.CharField(max_length=200)
    created_by = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Movie(models.Model):
    list = models.ForeignKey('movieapp.list', on_delete=models.CASCADE, related_name='movies')
    title = models.CharField(max_length=200)
    added_by = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    watched = models.BooleanField(default=False)

    def __str__(self):
        return self.title
