from typing import List

from core.database import Base
from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True, index=True)
    username = mapped_column(String, index=True, nullable=False, unique=True)
    hashed_password = mapped_column(String, nullable=False)
    email = mapped_column(String, nullable=False, unique=True)
    full_name = mapped_column(String, nullable=False)
    disabled = mapped_column(Boolean, nullable=False)

    posts: Mapped[List["Post"]] = relationship()