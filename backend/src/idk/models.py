from __future__ import annotations

from sqlalchemy import ForeignKey, Index, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from idk.database import Base


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(320), nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="active")
    role: Mapped[str] = mapped_column(String(20), nullable=False, default="user")

    profile: Mapped["Profile"] = relationship(
        back_populates="account",
        cascade="all, delete-orphan",
    )


class Profile(Base):
    __tablename__ = "profiles"

    account_id: Mapped[int] = mapped_column(
        ForeignKey("accounts.id"), primary_key=True
    )
    display_name: Mapped[str] = mapped_column(String(50), nullable=False)
    avatar_path: Mapped[str | None] = mapped_column(String(500), nullable=True)

    account: Mapped[Account] = relationship(back_populates="profile")


Index("uq_accounts_email_lower", func.lower(Account.email), unique=True)
