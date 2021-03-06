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
            print(1)
            ee = upload.save(commit=False)
            print(2)
            uu = request.user
            print(3)
            profiles = Profile.objects.all()
            print(profiles)
            for p in profiles:
                print(5)
                print(uu)
                if (p.user == uu):
                    ee.createBy = p
                    print(6)
            print(7)
            ee.save()
            return redirect('exerciseIndex')
        else:
            print(8)
            return HttpResponse("""your form is wrong""")
    else:

            return render(request, 'exercise/upload.html', {'upload_form':upload})


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
                    ee.createBy = p
            ee.save()
            ee.save()
            return redirect('VideoIndex')
        else:
            return HttpResponse("""your form is wrong""")
    else:
        return render(request, 'Video/upload.html', {'upload_form': upload})