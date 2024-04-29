from django.urls import re_path as url
from . import consumers

websocket_urlpatterns = [
    url(r"wsdemo/(?P<device>\w+)/$", consumers.ChatConsumer.as_asgi()),
]
