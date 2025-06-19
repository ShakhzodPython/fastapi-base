from fastapi_users import schemas

from core.shared_types.user_id import UserIdType


# from pydantic import BaseModel, ConfigDict

# Base schema of users
# class UserBase(BaseModel):
#     username: str
#     foo: int
#     bar: int
#
#
# class UserCreate(UserBase):
#     pass
#
#
# class UserRead(UserBase):
#     model_config = ConfigDict(
#         from_attributes=True,
#     )
#
#     id: int


# Schema for fastapi-users
class UserRead(schemas.BaseUser[UserIdType]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass

