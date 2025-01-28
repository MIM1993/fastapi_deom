from pydantic import BaseModel
from typing import Optional


# 请求参数格式
class LoginRequest(BaseModel):
    UserName: str
    PassWord: str


# 返回参数格式
class LoginResponse(BaseModel):
    code: int
    message: str
    data: Optional[str] = None
