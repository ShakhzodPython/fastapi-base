import asyncio
import contextlib
from os import getenv

from api.dependecies.authentication.manager import get_user_manager
from api.dependecies.authentication.users import get_users_db

from core.authentication.manager import UserManager
from core.models import db_helper
from core.schemas.user import UserCreate

get_users_db_context = contextlib.asynccontextmanager(get_users_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)

default_email = getenv("DEFAULT_EMAIL", "admin@admin.com")
default_password = getenv("DEFAULT_PASSWORD", "abc")
default_is_active = True
default_is_superuser = True
default_is_verified = True


async def create_user(
    user_manager: UserManager,
    user_create: UserCreate,
):
    user = await user_manager.create(user_create=user_create, safe=False)
    return user


async def create_superuser(
    email: str = default_email,
    password: str = default_password,
    is_active: bool = default_is_active,
    is_superuser: bool = default_is_superuser,
    is_verified: bool = default_is_verified,
):
    user_create = UserCreate(
        email=email,
        password=password,
        is_active=is_active,
        is_superuser=is_superuser,
        is_verified=is_verified,
    )

    async with db_helper.session_factory() as session:
        async with get_users_db_context(session) as user_db:
            async with get_user_manager_context(user_db) as user_manager:
                user = await user_manager.create(
                    user_create=user_create,
                )
                return user


if __name__ == "__main__":
    asyncio.run(create_superuser())
