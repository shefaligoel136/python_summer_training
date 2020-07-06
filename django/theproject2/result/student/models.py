from django.db import models

# Create your models here.

class students(models.Model):
 sname = models.CharField(max_length = 100)# charfield comes from Model
 spassword = models.CharField(max_length = 100)
 srollnum = models.CharField(max_length = 100)