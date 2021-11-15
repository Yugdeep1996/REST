from django.db import models

# Create your models here.

class Singer(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='sungby', null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title