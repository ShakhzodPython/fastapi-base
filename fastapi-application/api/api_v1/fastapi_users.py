from fastapi_users import FastAPIUsers

from core.models import User
from core.shared_types.user_id import UserIdType

from api.dependecies.authentication import (
    get_user_manager,
    authentication_backend,
)

fastapi_users = FastAPIUsers[User, UserIdType](
    get_user_manager, [authentication_backend]
)

current_user = fastapi_users.current_user(active=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)
