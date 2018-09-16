from django import forms
from django.db import models
from datetime import datetime

# Create your models here.

class posts(models.Model):
	title = models.CharField(max_length=255)
	body = models.TextField()
	count = models.IntegerField(default=0)
	created_at = models.DateTimeField(default=datetime.now, blank=True)
	event_date = models.CharField(max_length=255)
	def __str__(self):
		return self.title
	class Meta:
		verbose_name_plural = "Posts"

class Amice(models.Model):
	post = models.ForeignKey(posts, on_delete=models.CASCADE, related_name = 'aanwezigen')
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	lichting = models.IntegerField()
	class Meta:
		unique_together = ["first_name", "last_name", "lichting"]
		verbose_name_plural = "Amici"


	def __str__(self):
		return "%s %s %s" % (self.first_name, self.last_name, self.lichting)


