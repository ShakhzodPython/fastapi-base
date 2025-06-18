from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependecies.authentication.backend import authentication_backend
from api.dependecies.authentication.fastapi_users import fastapi_users

from core.crud import users as users_crud
from core.models import db_helper
from core.schemas.user import UserRead, UserCreate

router = APIRouter(tags=["Users"])


@router.get("", response_model=list[UserRead], include_in_schema=False)
async def get_users(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    users = await users_crud.get_users(session=session)
    return users


@router.post("/create", response_model=UserRead, include_in_schema=False)
async def create_user(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    user_create: UserCreate,
):
    user = await users_crud.create_user(
        session=session,
        user_create=user_create,
    )
    return user


# Router for auth user through fastapi-users
router.include_router(
    router=fastapi_users.get_auth_router(backend=authentication_backend),
)