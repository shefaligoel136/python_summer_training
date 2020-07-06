from django.db import models

class faculty_login(models.Model):
	fname = models.CharField(max_length=100)
	fpass = models.CharField(max_length=100)

