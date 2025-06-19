from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer

from core.config import settings
from .users import router as users_router
from .auth import router as auth_router
from .messages import router as messages_router

http_bearer = HTTPBearer(
    auto_error=False,
)

router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(
    auth_router,
    prefix=settings.api.v1.auth,
    dependencies=[Depends(http_bearer)],
)

router.include_router(
    users_router,
    prefix=settings.api.v1.users,
)

router.include_router(
    messages_router,
    prefix=settings.api.v1.messages,
)
