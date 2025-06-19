from typing import Annotated

from fastapi import APIRouter, Depends

from core.models import User
from core.schemas.user import UserRead
from .fastapi_users import current_user, current_superuser

router = APIRouter(
    tags=["Messages"],
)


@router.get("")
def get_user_messages(
    user: Annotated[User, Depends(current_user)],
):
    return {
        "messages": ["m1", "m2", "m3"],
        "user": UserRead.model_validate(user),
    }

@router.get("/secrets")
def get_superuser_messages(
    user: Annotated[User, Depends(current_superuser)],
):
    return {
        "messages": ["secrets-m1", "secrets-m2", "secrets-m3"],
        "user": UserRead.model_validate(user),
    }
