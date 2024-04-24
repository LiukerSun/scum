from datetime import datetime

import jwt
from rest_framework.response import Response
from django.conf import settings

from auth import models
from libs.custom_logger import logger
from libs.exceptions import HTTP401, HTTP403

JWT_TOKEN = settings.JWT_TOKEN


"""函数"""


# 解析jwt
def decode_jwt(token: str, key: str):
    try:
        return jwt.decode(token, key, algorithms=["HS256"])
    except:
        raise HTTP403


def get_id_from_jwt(token: str, key: str):
    try:
        user_dict = jwt.decode(token, key, algorithms=["HS256"])
        user_id = user_dict.get("user_id")
        return user_id
    except:
        raise HTTP403


"""装饰器"""


# 日志打印装饰器。记录接口调用信息。
def api_log(func):
    def wrapper(self, request, *args, **kwargs):
        logger.info(
            rf"""   
                    time: {datetime.utcnow()}
                    path:{request.path}
                    method:{request.method}
                    data: {request.data}
                    header:{request.headers}
                    get:{request.GET}
                    """
        )
        result = func(self, request, *args, **kwargs)
        return result

    return wrapper


# POST 请求BODY参数校验装饰器。
def validate_body_params(required_params):
    def decorator(view_func):
        def wrapper(self, request, *args, **kwargs):
            # 验证请求体中是否包含必需的参数
            missing_params = [
                param for param in required_params if param not in request.data
            ]
            if missing_params:
                return Response(
                    {"error": f'body缺少参数: {", ".join(missing_params)}'},
                    status=400,
                )
            # 如果所有参数都存在，继续执行视图函数
            return view_func(self, request, *args, **kwargs)

        return wrapper

    return decorator


# GET 请求查询参数校验装饰器。
def validate_get_params(required_params):
    def decorator(view_func):
        def wrapper(self, request, *args, **kwargs):
            # 验证请求中是否包含必需的查询参数
            missing_params = [
                param for param in required_params if param not in request.GET
            ]
            if missing_params:
                return Response(
                    {"error": f'GET请求缺少参数: {", ".join(missing_params)}'},
                    status=400,
                )
            # 如果所有参数都存在，继续执行视图函数
            return view_func(self, request, *args, **kwargs)

        return wrapper

    return decorator


# 检查是否存在 user token
def check_user_token(func):
    def wrapper(self, request, *args, **kwargs):
        user_token = request.headers.get("Authorization", "")
        if user_token:
            user_dict = decode_jwt(user_token, JWT_TOKEN)
            user_id = user_dict.get("user_id")
            if models.User.objects.filter(id=user_id).exists():
                result = func(self, request, *args, **kwargs)
                return result
            else:
                raise HTTP401
        else:
            raise HTTP401

    return wrapper
