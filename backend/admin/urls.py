from django.urls import include
from django.urls import re_path as url

urlpatterns = [
    url(r"^account/", include("auth.urls")),
    url(r"^device/", include("device.urls")),
]
