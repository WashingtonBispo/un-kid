from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from datetime import datetime
from pydantic import BaseModel
from .base import Base

class Transaction(Base):
    __tablename__ = "TRANSACTION"
    id: Mapped[str] = mapped_column(String(50), primary_key=True)
    origin: Mapped[str] = mapped_column(String(60))
    value: Mapped[int] = mapped_column()
    day: Mapped[datetime] = mapped_column(
    )
    accountId: Mapped[str] = mapped_column(ForeignKey("ACCOUNT.id"))
    account: Mapped["Account"] = relationship(back_populates="transactions")
    def __repr__(self) -> str:
        return f"id={self.id!r}, Origem={self.origem!r}, Valor={self.valor!r}, Dia={self.dia!r})"

class TransactionJSON(BaseModel):
    origin: str
    value: int
    accountId: str
    day: datetime