from django import forms
from .models import Exercise , Video, SubmitedExercise

class ExerciseCreate(forms.ModelForm):
    class Meta:
        model=Exercise
        fields=["id","exersizename","detai","exercisefile","date"]
class VideoCreate(forms.ModelForm):
    class Meta:
        model=Video
        fields=["id","videozename","detai","videofile"]

class submitExerciseCreate(forms.ModelForm):
            class Meta:
                model = SubmitedExercise
                fields = ["id", "score", "file"]