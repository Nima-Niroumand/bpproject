from django.conf.urls import url,include
from django.urls import path
from education.views import dashboard, exerciseIndex ,exerciseUpload,VideoUpload,videoIndex,downloadExerciseFiles,sendExercise,submitedExerciseIndex,videoPlay
from education.views import submitExerciseIndex,sendExercise,downloadSubmitedExerciseFiles
urlpatterns = [
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^exercise/index/",exerciseIndex,name="exerciseIndex"),
    url(r"^exercise/upload/",exerciseUpload,name="exerciseUpload"),
    url(r"^video/index/", videoIndex, name="videoIndex"),
    url(r"^video/upload/",VideoUpload,name="VideoUpload"),
    path("exercise/download/exerciseFiles/<str:path>", downloadExerciseFiles, name="downloadExerciseFiles"),
    path("video/play/<int:id>", videoPlay, name="videoPlay"),
    path("submitExercise/index/",submitExerciseIndex,name="submitExerciseIndex"),
    path("submitExercise/sendExercise/<int:ExeId>",sendExercise,name="sendExercise"),
    path("submitExercise/download/exerciseFiles/<str:path>", downloadExerciseFiles, name="downloadExerciseFiles"),
]
