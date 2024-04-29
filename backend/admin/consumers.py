import json
import time
from django.core.cache import caches
from channels.generic.websocket import WebsocketConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from loguru import logger


class ChatConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.device_connected = False

    def connect(self):
        self.accept()
        self.device = self.scope["url_route"]["kwargs"]["device"]  # 获取设备信息
        device_added = caches["devices"].add(self.device, self.device)  # 尝试添加设备
        if not device_added:
            # 设备已连接，拒绝连接
            self.send(text_data="设备已存在！")
            self.close()
        else:
            # 设备未连接，允许连接并添加到组
            self.channel_layer = get_channel_layer()
            async_to_sync(self.channel_layer.group_add)(
                self.device, self.channel_name  # 将设备信息作为组名
            )
            self.device_connected = True

    def disconnect(self, close_code):
        if self.device_connected:
            caches["devices"].delete(self.device)
            async_to_sync(self.channel_layer.group_discard)(
                self.device, self.channel_name  # 将设备信息作为组名
            )
        self.device_connected = False

    def receive(self, text_data):
        order_data_json = json.loads(text_data)
        order_data_json["device"] = self.device
        logger.info(
            f"Received message for a different device ({order_data_json}), ignoring."
        )

    def send_message(self, event):
        self.send(text_data=json.dumps({"message": event["message"]}))
