from fastapi import APIRouter

from api.v1.fastapi_users import fastapi_users
from api.dependecies.authentication.backend import authentication_backend

from core.schemas.user import UserRead, UserCreate

router = APIRouter(tags=["Auth"])

# Router for login/logout user through fastapi-users
router.include_router(
    router=fastapi_users.get_auth_router(
        backend=authentication_backend,
    ),
)


# Router for register user through fastapi-users
router.include_router(
    router=fastapi_users.get_register_router(
        UserRead,
        UserCreate,
    ),
)

# Router for verify token and email
router.include_router(
    router=fastapi_users.get_verify_router(
        UserRead,
    ),
)


# Router for forgot password and reset password

router.include_router(
    router=fastapi_users.get_reset_password_router(),
)
