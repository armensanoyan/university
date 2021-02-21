from django.db import models

class Universities(models.Model):
	name = models.CharField( max_length=50)
	address = models.CharField(max_length=50)
	subjects = models.TextField()
	def __str__(self):
		return self.name