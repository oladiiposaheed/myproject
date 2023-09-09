from django.db import models

# Create your models here.
class StudentInfo3(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    age = models.IntegerField()
    math = models.IntegerField()
    chem = models.IntegerField()
    phy = models.IntegerField()
    bio = models.IntegerField()
    td = models.IntegerField()
    eng = models.IntegerField()
