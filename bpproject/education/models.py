from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    student_number=models.CharField(max_length=10)
    isStudent=models.BooleanField()

class Exercise(models.Model):
    professor=models.ForeignKey(Profile,on_delete=models.CASCADE)
    exersizename=models.CharField(max_length=200)
    date=models.DateTimeField(editable=False)
    detai=models.CharField(max_length=1000)
    exercisefile=models.FileField(upload_to='exercisefile/')


class Video(models.Model):
    professor_video = models.ForeignKey(Profile, on_delete=models.CASCADE)
    videozename = models.CharField(max_length=200)
    detai = models.CharField(max_length=1000)
    videofile = models.FileField(upload_to='exercisefile/')

class SubmitedExercise(models.Model):
   exercise=models.ForeignKey(Exercise,on_delete=models.CASCADE)
   student=models.ForeignKey(Profile,on_delete=models.CASCADE)
   score=models.IntegerField()