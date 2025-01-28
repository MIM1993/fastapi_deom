from typing import Union, List, Optional
from pydantic import BaseModel


# 请求参数格式
class ItemRequest(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


# 自定义数据字段
class ItemData(BaseModel):
    rtsp_addr: str
    model_path: str
    video_path: str


# 返回参数格式
class ItemResponse(BaseModel):
    code: int
    message: str
    data: Optional[ItemData]
