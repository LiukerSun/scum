from rest_framework import status
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if not hasattr(response, "status_code"):
        return response

    if response.status_code == status.HTTP_400_BAD_REQUEST:
        response.data["detail"] = "请求参数错误"
    elif response.status_code == status.HTTP_401_UNAUTHORIZED:
        response.data["detail"] = "用户未登录或用户非法"
    elif response.status_code == status.HTTP_403_FORBIDDEN:
        response.data["detail"] = "没有访问权限"
    elif response.status_code == status.HTTP_404_NOT_FOUND:
        response.data["detail"] = "请求资源不存在"
    elif response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED:
        response.data["detail"] = "请求方法不允许"
    elif response.status_code == status.HTTP_409_CONFLICT:
        response.data["detail"] = "已存在，创建失败"
    elif response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR:
        response.data["detail"] = "服务器内部错误"

    return response


class HTTP400(APIException):
    """请求参数错误"""

    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "请求参数错误"


class HTTP401(APIException):
    """用户未登录或用户非法"""

    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "用户未登录或用户非法"


class HTTP403(APIException):
    """没有访问权限"""

    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "没有访问权限"


class HTTP404(APIException):
    """请求资源不存在"""

    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "请求资源不存在"


class HTTP409(APIException):
    """已存在"""

    status_code = status.HTTP_409_CONFLICT
    default_detail = "已存在"


class HTTP500(APIException):
    """服务器内部错误"""

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "服务器内部错误"
