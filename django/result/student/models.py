from django.db import models

# Create your models here.
class students(models.Model):
	rollnum = models.CharField(max_length=100)
	sname = models.CharField(max_length=100)
	spass = models.CharField(max_length=100)
	marks = models.CharField(max_length=100)

