from fastapi import APIRouter
from controller_params.item import ItemRequest, ItemResponse, ItemData

item_router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)


@item_router.get("/get")
async def read_items():
    data = ItemData(model_path="/xxx/xxx/xxx", rtsp_addr="rtsp://192.168.52.71:8880/123/xxx", video_path="test.mp3")
    fake_items_db = ItemResponse(code=200, data=data, message="success")
    return fake_items_db.model_dump()


@item_router.post("/post")
async def read_items(rsq: ItemRequest):
    print(rsq.model_dump_json())
    return {"code": 0, "messages": "success", "data": rsq.model_dump()}
