from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import router
from global_info import InitDB

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)

db = InitDB("mysql")
db.create_all()


@app.get("/health/check")
def read_root():
    return {"ping": "pong"}
