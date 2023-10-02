from pydantic import EmailStr

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class User(DeclarativeBase):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    email: Mapped[EmailStr] = mapped_column(
        nullable=False,
        index=True,
        unique=True
    )
    password_hash: Mapped[str] = mapped_column(
        nullable=False
    )

    firstname: Mapped[str] = mapped_column(String(30))
    lastname: Mapped[str] = mapped_column(String(30))
    company: Mapped[str] = mapped_column(String(30))
