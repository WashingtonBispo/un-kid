from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from .base import Base

class Classroom(Base):
    __tablename__ = "CLASSROOM"
    id: Mapped[str] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(30))
    imagem: Mapped[str] = mapped_column()
    accounts: Mapped[List["Account"]] = relationship(
        back_populates="classroom",
        cascade="all, delete-orphan"
    )
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.nome!r}"

class ClassroomJSON(BaseModel):
    nome: str
    imagem: str

