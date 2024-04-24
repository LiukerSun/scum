import os
import jwt
import hmac
import hashlib


# 加密密码
def hash_password(password: str) -> tuple[bytes, bytes]:
    # 生成64位盐
    salt: bytes = os.urandom(8)
    # 初始哈希
    hashed = hmac.new(salt, password.encode("utf-8"), hashlib.sha256).digest()
    # 叠代混淆
    for _ in range(10):
        hashed = hmac.new(salt, hashed, hashlib.sha256).digest()
    salt = salt.hex()
    hashed = hashed.hex()
    return salt, hashed


# 校验密码
def check_password(password: str, salt: str, hashed: str) -> bool:
    # 检查密码是否正确
    hashed2 = hmac.new(
        bytes.fromhex(salt), password.encode("utf-8"), hashlib.sha256
    ).digest()
    for _ in range(10):
        hashed2 = hmac.new(bytes.fromhex(salt), hashed2, hashlib.sha256).digest()
    hashed2 = hashed2.hex()
    return hashed == hashed2


# 生成jwt
def encode_jwt(payload: dict, key: str) -> str:
    return jwt.encode(payload, key, algorithm="HS256")
