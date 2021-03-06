from django import forms
from .models import Exercise , Video

class ExerciseCreate(forms.ModelForm):
    class Meta:
        model=Exercise
        fields=["id","exersizename","detai","exercisefile","date"]
class VideoCreate(forms.ModelForm):
    class Meta:
        model=Video
        fields=["id","videozename","detai","videofile"]