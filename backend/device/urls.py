from django.urls import path
from . import views

command = views.DeviceView.as_view(
    {
        "post": "send_command",
    }
)
urlpatterns = [
    path(r"command", command),
]
