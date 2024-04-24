from django.db import models


# 用户表
class User(models.Model):
    id = models.AutoField(primary_key=True)  # 用户id
    username = models.CharField(max_length=50, unique=True)  # 用户名
    password = models.CharField(max_length=64)  # 密码 加盐加密
    salt = models.CharField(max_length=16)  # 盐
    admin = models.BooleanField(default=False)
    delete_flag = models.BooleanField(default=False)  # 删除标志位


# 用户信息表
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # 用户id
    avatar = models.CharField(max_length=128, blank=True)  # 头像
    email = models.CharField(max_length=64, blank=True)  # 邮箱
    phone = models.CharField(max_length=16, blank=True)  # 电话
    steam_id = models.CharField(max_length=16, blank=True)  # steamid
