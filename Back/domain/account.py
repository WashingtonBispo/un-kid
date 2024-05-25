from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from .base import Base
from pydantic import BaseModel
from sqlalchemy.inspection import inspect


class Account(Base):
    __tablename__ = "ACCOUNT"
    id: Mapped[str] = mapped_column(String(50), primary_key=True)
    nome: Mapped[str] = mapped_column(String(60))
    imagem: Mapped[str] = mapped_column()
    meta: Mapped[int] = mapped_column()
    senha: Mapped[str] = mapped_column(String(12))
    classroomId: Mapped[str] = mapped_column(ForeignKey("CLASSROOM.id"))
    classroom: Mapped["Classroom"] = relationship(back_populates="accounts")
    transactions: Mapped[List["Transaction"]] = relationship(
        back_populates="account", 
        cascade="all, delete-orphan"
    )
    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.nome!r})"

class AccountJSON(BaseModel):
    nome: str
    imagem: str
    meta: int
    senha: str
    classroomId: str