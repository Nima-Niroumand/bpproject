from django.shortcuts import render , redirect
from .models import Exercise,Profile,Video,SubmitedExercise
from .forms import ExerciseCreate ,VideoCreate,submitExerciseCreate
from django.http import HttpResponse ,Http404
import os
from django.conf import settings
from django.shortcuts import get_list_or_404, get_object_or_404
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


def videoPlay(request, id):
    video = Video.objects.get(id=id)
    print(video.videozename)

    return render(request, "video/play.html", {"video": video})
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

	file_path = os.path.join(settings.MEDIA_ROOT,"exerciseFiles", path)
	if os.path.exists(file_path):
		with open(file_path, 'rb') as fh:
			response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
			response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
			return response
	raise Http404
def submitedExerciseIndex(request):
    s=  SubmitedExercise.objects.all()
    return render(request, "submitExercise/index.html",{"submitExercises":s})
def selectUserProfile:
    profiles = Profile.objects.all()
    for p in profiles:
        if (p.user == uu):
            ee.student = p
def sendExercise(request, ExeId ):
    upload = submitExerciseCreate()
    exercise = get_object_or_404(Exercise, id=ExeId)
    if request.method == 'POST':
        upload = submitExerciseCreate(request.POST, request.FILES)
        if upload.is_valid():
            ee = upload.save(commit=False)
            uu = request.user
            profiles = Profile.objects.all()
            for p in profiles:
                if (p.user == uu):
                    ee.student = p
            ee.exercise  =exercise
            ee.score = -1
            ee.save()
            return redirect('submitExerciseIndex')
        else:
            print(upload.errors)
            return HttpResponse("""your form is wrong""")
    else:
        args = {}

        args['Id'] = id
        args['exercise'] = exercise
        args['upload_form'] = upload
        return render(request, 'submitExercise/sendExercise.html', args)

def submitExerciseIndex(request):
     exercises = Exercise.objects.all()
     submitedExercise = SubmitedExercise.objects.all()
     print(submitedExercise[1])
     args = {}
     args['submitedExercise']=submitedExercise;
     args['exercises']=exercises;

     return render(request, 'submitExercise/index.html', args)
def downloadSubmitedExerciseFiles(request, path):
	print(path)
	print(os.path.join(settings.MEDIA_ROOT,"file ", path))
	file_path = os.path.join(settings.MEDIA_ROOT,"file ", path)
	if os.path.exists(file_path):
		with open(file_path, 'rb') as fh:
			response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
			response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
			return response
	raise Http404