from django.shortcuts import render , redirect
from .models import Exercise,Profile,Video
from .forms import ExerciseCreate ,VideoCreate
from django.http import HttpResponse
import os
from django.conf import settings

def dashboard(request):
    args = {}

    profiles = Profile.objects.all()

    uu = request.user
    for p in profiles:
        if (p.user == uu):
            if (p.isStudent == True):
                args['isStudent'] = True
            else:
                args['isStudent'] = False

    print(profiles)

    return render(request, "users/dashboard.html", args)
def exerciseIndex(request):
    exercises = Exercise.objects.all()
    return render(request, "exercise/index.html",{"exercises":exercises})
def exerciseUpload(request):
    upload = ExerciseCreate()

    if request.method == 'POST':

        upload = ExerciseCreate(request.POST, request.FILES)
        if upload.is_valid():

            ee = upload.save(commit=False)

            uu = request.user

            profiles = Profile.objects.all()

            for p in profiles:
                if (p.user == uu):
                    ee.professor= p


            ee.save()
            return redirect('exerciseIndex')
        else:

            return HttpResponse("""your form is wrong""")
    else:

            return render(request, 'exercise/upload.html', {'upload_form':upload})
def videoIndex(request):
    videos = Video.objects.all()
    return render(request, "video/index.html",{"videos":videos})

def VideoUpload(request):
    upload = VideoCreate()
    if request.method == 'POST':
        upload = VideoCreate(request.POST, request.FILES)
        if upload.is_valid():
            ee = upload.save(commit=False)
            uu = request.user
            profiles = Profile.objects.all()
            for p in profiles:
                if (p.user == uu):
                    ee.professor_video = p
            ee.save()
            return redirect('videoIndex')
        else:
            return HttpResponse("""your form is wrong""")
    else:
        return render(request, 'video/upload.html', {'upload_form': upload})