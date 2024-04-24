import time

from loguru import logger
from rest_framework.response import Response
from django.conf import settings

from auth import models, serializers
from libs.baseView import BaseViewSet
from libs.exceptions import HTTP401, HTTP409
from libs.custom_functions import (
    api_log,
    validate_body_params,
    check_user_token,
    decode_jwt,
)
from auth.libs.auth_functions import hash_password, check_password, encode_jwt

JWT_TOKEN = settings.JWT_TOKEN


class UserViewSet(BaseViewSet):
    model = models.User
    queryset = model.objects.all()
    serializer_class = serializers.UserSerializer

    @api_log
    @validate_body_params(["username", "password"])
    def login(self, request, *args, **kwargs):
        username = request.data["username"]
        password = request.data["password"]
        user = self.queryset.filter(username=username).first()
        if user:
            if not check_password(password, user.salt, user.password):
                raise HTTP401
            else:
                user_id = user.id
                is_admin = user.admin

                payload = {
                    "user_id": user_id,
                    "username": username,
                    "is_admin": is_admin,
                    "exp": time.time() + 18000,
                }
                user_token = encode_jwt(payload, JWT_TOKEN)
                # get user profile

                response = Response(
                    {
                        "user_token": user_token,
                    },
                    status=200,
                )
                response = self.response_proxy(response)
                return response
        else:
            time.sleep(1)
            raise HTTP401

    @api_log
    @validate_body_params(["username", "password"])
    def register(self, request, *args, **kwargs):
        username: str = request.data["username"]
        password: str = request.data["password"]
        # check user exist
        if self.queryset.filter(username=username).exists():
            raise HTTP409
        else:
            salt, password = hash_password(password)
            # create User
            user = models.User.objects.create(
                username=username, password=password, salt=salt
            )
            user.save()
            # create User Profile
            models.UserProfile.objects.create(user=user).save()
            response = Response({}, status=201)
            response = self.response_proxy(response)
            return response

    @api_log
    @check_user_token
    def get_user_profile(self, request, *args, **kwargs):
        user_token = request.headers.get("Authorization", "")
        if user_token:
            user_dict = decode_jwt(user_token, JWT_TOKEN)
            user_id = user_dict.get("user_id")
            username = user_dict.get("username")
            isAdmin = "admin" if user_dict["is_admin"] else "user"
            user_profile = models.UserProfile.objects.filter(user_id=user_id).first()
            profile = serializers.UserProfileSerializer(user_profile).data
            profile["username"] = username
            profile["access"] = isAdmin
            response = Response(
                {
                    "user_profile": profile,
                },
                status=200,
            )
            response = self.response_proxy(response)
            return response
        else:
            time.sleep(1)
            raise HTTP401
