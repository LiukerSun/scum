from django.urls import path
from . import views


auth = views.UserViewSet.as_view(
    {
        "post": "login",
        "put": "register",
        "get": "get_user_profile",
    }
)
urlpatterns = [
    path(r"auth", auth),
]
