from django.db import models

# Create your models here.
 
class Notes(models.Model):
    text = models.CharField(max_length=2000)
    tag = models.CharField(max_length=15 , blank=True)
    created = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)