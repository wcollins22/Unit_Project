from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=100)
    fav_genre = models.CharField(max_length=50)
    dream = models.CharField(max_length=100)
    job = models.CharField(max_length=50)
    hometown = models.CharField(max_length=50)