from django.db import models

# Create your models here.
class Log(models.Model):
	filename = models.CharField(max_length=30)
	use_time = models.TimeField()
	address = models.IPAddressField()

