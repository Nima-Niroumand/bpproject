from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    student_number=models.TextField(max_length=10,blank=True)
    isStudent=models.BooleanField()

class Exercise(models.Model):
    professor=models.ForeignKey(Profile,on_delete=models.CASCADE)
    exersizename=models.CharField(max_length=200)
    date=models.DateTimeField(editable=True)
    detai=models.CharField(max_length=1000)
    exercisefile=models.FileField(upload_to='exerciseFiles/')
    id=models.AutoField(primary_key=True)


class Video(models.Model):
    professor_video = models.ForeignKey(Profile, on_delete=models.CASCADE)
    videozename = models.CharField(max_length=200)
    detai = models.CharField(max_length=1000)
    videofile = models.FileField(upload_to='videos/')
    id = models.AutoField(primary_key=True)

class SubmitedExercise(models.Model):
   exercise=models.ForeignKey(Exercise,on_delete=models.CASCADE)
   student=models.ForeignKey(Profile,on_delete=models.CASCADE)
   score = models.DecimalField(decimal_places=2,max_digits=4,null=True,blank=True)
   id = models.AutoField(primary_key=True)
   file = models.FileField(upload_to='submitedExerciseFiles/')
