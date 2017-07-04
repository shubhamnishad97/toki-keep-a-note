from django.db import models
from django.conf import settings


# Create your models here.
 
class Notes(models.Model):
	label = models.CharField(max_length=200)
	body = models.TextField(max_length=20000)
	timestamp = models.DateTimeField(auto_now_add=True)
	tags = models.ManyToManyField('Tag', related_name='notes', blank=True)
	owner = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="notes_owner",blank=True,null=True)
	def __str__(self):
		return self.label
		



class Tag(models.Model):
	label = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200)
	def __str__(self):
		return self.label







