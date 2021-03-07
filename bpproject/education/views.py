from django.shortcuts import render , redirect
from .models import Exercise,Profile,Video
from .forms import ExerciseCreate ,VideoCreate
from django.http import HttpResponse ,Http404
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


def downloadExerciseFiles(request, path):
	print(path)
	print(os.path.join(settings.MEDIA_ROOT,"exerciseFiles", path))
	file_path = os.path.join(settings.MEDIA_ROOT,"exerciseFiles", path)
	if os.path.exists(file_path):
		with open(file_path, 'rb') as fh:
			response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
			response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
			return response
	raise Http404