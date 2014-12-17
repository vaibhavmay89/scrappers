from django.db import models

# Create your models here.
class post(models.Model):
	title = models.CharField(max_length = 100)
	body = models.TextField()
	date = models.DateTimeField()

	def __unicode__(self):
		return self.title