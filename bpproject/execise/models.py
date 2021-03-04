from django.db import models
from django.contrib.auth.models import User

class Exercise(models.Model):
    professor=models.ForeignKey(User)
    exersizename=models.CharField(max_length=200)
    date=models.DateTimeField(editable=False)
    detai=models.CharField(max_length=1000)
    exercisefile=models.CharField(max_length=1000)
