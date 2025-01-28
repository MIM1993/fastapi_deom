from fastapi import APIRouter
from controller_params.login import LoginRequest, LoginResponse

login_router = APIRouter(
    prefix="/api",
    tags=["login"],
    responses={404: {"description": "Not found"}},
)


@login_router.post("/login")
async def read_items(rsq: LoginRequest):
    print(rsq.model_dump_json())
    rsp = LoginResponse(code=0, message="success", data="登陆成功！！！")
    return rsp.model_dump()
