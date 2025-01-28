from pydantic import BaseSettings, validator, IPvAnyAddress, EmailStr, AnyHttpUrl


class Config(BaseSettings):
    server_url = "127.0.0.1:5000"
    server_port = 5000

    mysql_url = "127.0.0.1:3306"

