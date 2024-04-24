from django.urls import include
from django.urls import re_path as url

urlpatterns = [
    url(r"^account/", include("auth.urls")),
]
