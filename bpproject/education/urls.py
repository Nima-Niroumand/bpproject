from django.conf.urls import url,include
from education.views import dashboard, exerciseIndex ,exerciseUpload,VideoUpload

urlpatterns = [
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^exercise/index/",exerciseIndex,name="exerciseIndex"),
    url(r"^exercise/upload/",exerciseUpload,name="exerciseUpload"),
    url(r"^Video/upload/",VideoUpload,name="VideoUpload")
]