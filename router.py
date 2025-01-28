from fastapi import APIRouter
from controller.Item import item_router
from controller.login import login_router

# 添加controller中的路由
router = APIRouter()
router.include_router(item_router)
router.include_router(login_router)
