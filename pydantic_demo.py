#! -*-conding: UTF-8 -*-
# @公众号: 海哥python
import json
from enum import Enum

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, EmailStr, field_validator, Field, validate_call, computed_field
# 导入pydantic对应的模型基类
from pydantic import constr, conint
from typing import Annotated


class GenderEnum(str, Enum):
    """
    性别枚举
    """
    male = "男"
    female = "女"


class test(Enum):
    male = "男"
    female = "女"


class User(BaseModel):
    id: int
    name: str = "小卤蛋"
    age: conint(ge=0, le=99)  # 整数范围：0 <= age <= 99
    email: EmailStr
    signup_ts: Optional[datetime] = None
    friends: List[str] = []
    password: constr(min_length=6, max_length=10)  # 字符长度
    phone: constr(pattern=r'^1\d{10}$')  # 正则验证手机号
    sex: GenderEnum  # 枚举验证, 能传: 男和女

    @field_validator("name")
    @classmethod
    def check_name(cls, name: str) -> str:
        """Validator to be used throughout"""
        if not name.startswith("小"):
            raise ValueError("must be startswith 小")
        return name

    @field_validator("age")
    @classmethod
    def check_age(cls, age):
        if age < 18:
            raise ValueError("用户年龄必须大于18岁")
        return age

    @computed_field  # 计算属性
    @property
    def link(self) -> str:
        return f"尼古拉斯 · {self.name}"


class Person(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    age: int = Field(..., gt=0, lt=20)


@validate_call
def greet(person: Person, message: Annotated[int, Field(gt=1, lt=100)]):
    print(f"Hello, {person.name}! {message}")


# 正确的调用
# greet(Person(name="公众号：海哥python", age=18), "How are you?")
greet(Person(name="公众号：海哥python", age=18), 10)

if __name__ == '__main__':

    user_data = {
        "id": 123,
        "name": "小卤蛋",
        "age": 20,
        "email": "xiaoludan@example.com",
        'signup_ts': '2024-07-19 00:22',
        'friends': ["公众号：海哥python", '小天才', b''],
        'password': '123456',
        'phone': '13800000000',
        'sex': '男'
    }

    try:
        # user = User(**user_data)
        user = User.model_validate(user_data)
        # print(f"User id: {user.   id}, User name: {user.name}, User email: {user.email}, friends: {user.friends}")
        print(user.model_dump_json())
        dumps_str = json.dumps(user)
        print(dumps_str)
    except ValidationError as e:
        print(f"Validation error: {e.json()}")
