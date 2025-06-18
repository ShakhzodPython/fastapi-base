from typing import TYPE_CHECKING

from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase


# from sqlalchemy import UniqueConstraint
# from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins.pk import PKMixin
from core.types.user_id import UserIdType

# Base example
# class User(PKMixin, Base):
#     username: Mapped[str] = mapped_column(unique=True)
#     foo: Mapped[int]
#     bar: Mapped[int]
#
#     __table_args__ = (
#         UniqueConstraint(
#             "foo",
#             "bar",
#         ),
#     )


if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


# Example with fastapi-users
class User(
    Base,
    PKMixin,
    SQLAlchemyBaseUserTable[UserIdType],
):
    pass

    @classmethod
    def get_db(
        cls,
        session: AsyncSession,
    ):
        return SQLAlchemyUserDatabase(session, User)
