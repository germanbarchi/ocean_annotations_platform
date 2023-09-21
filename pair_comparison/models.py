from django.db import models
from mimetypes import init
from django.contrib.auth.models import User
from datetime import datetime
from django import forms

CHOICES = [('Izquierda', 'Izquierda'), ('Derecha', 'Derecha')]

class Audio(models.Model):
    audiofile = models.FileField(upload_to='audios/')
    name = models.CharField(max_length=255)
    speaker_id = models.IntegerField(null=True)
    
    def __str__(self):
        return self.name
    
    
class Annotation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audio_A = models.ForeignKey(Audio, on_delete=models.CASCADE, related_name='A', blank=True, null=True)
    audio_B = models.ForeignKey(Audio, on_delete=models.CASCADE, related_name='B', blank=True, null=True)
    order = models.IntegerField()
    dim_O = models.CharField(max_length = 20, choices = CHOICES, null=True, blank=True)
    dim_C = models.CharField(max_length = 20, choices = CHOICES, null=True, blank=True)
    dim_E = models.CharField(max_length = 20, choices = CHOICES, null=True, blank=True)
    dim_A = models.CharField(max_length = 20, choices = CHOICES, null=True, blank=True)
    dim_N = models.CharField(max_length = 20, choices = CHOICES, null=True, blank=True)
    submit = models.BooleanField(default=False)
    mod_time = models.DateTimeField(auto_now=True)
    