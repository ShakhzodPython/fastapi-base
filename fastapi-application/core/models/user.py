from fastapi_users.db import SQLAlchemyBaseUserTable

from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins.pk import PKMixin

# Base example
class User(PKMixin, Base):
    username: Mapped[str] = mapped_column(unique=True)
    foo: Mapped[int]
    bar: Mapped[int]

    __table_args__ = (
        UniqueConstraint(
            "foo",
            "bar",
        ),
    )


# Example with fastapi-users
# class User(Base, PKMixin, SQLAlchemyBaseUserTable[int]):
#     pass

