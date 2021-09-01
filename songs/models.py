from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy


# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=64)
    genre = models.TextField(default="")
    purchaser = models.ForeignKey(get_user_model(), related_name='snacks', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('song-detail', args = [self.pk])