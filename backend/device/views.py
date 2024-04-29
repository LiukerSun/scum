from loguru import logger
from rest_framework.response import Response
from libs.baseView import BaseViewSet
from libs.exceptions import *
from libs.custom_functions import (
    api_log,
    validate_body_params,
    check_user_token,
    decode_jwt,
)
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.core.cache import caches


# views.py
class DeviceView(BaseViewSet):

    @api_log
    @validate_body_params(["device", "message"])
    def send_command(self, request, *args, **kwargs):
        data = request.data
        device = data.get("device")
        # check device
        if caches["devices"].has_key(device):
            message = data.get("message")
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                device,
                {"type": "send_message", "message": message, "device": device},
            )
            return Response("WebSocket message sent.")
        else:
            return Response("Device not found.", status=400)
