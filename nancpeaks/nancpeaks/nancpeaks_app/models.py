from django.db import models

# Create your models here.
class Speech(models.Model):
    text = models.CharField(max_length=1000)
    audio = models.FileField(upload_to='media/')