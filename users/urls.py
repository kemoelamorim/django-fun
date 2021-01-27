from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    url(r"^accounts/", include("django.contrib.auth.urls")),
]