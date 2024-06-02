from .context import engine
from ..domain.account import Account
from ..domain.transaction import Transaction
from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import HTTPException
from sqlalchemy.orm import joinedload
from sqlalchemy import func
import datetime
import uuid

def post(json):
    with Session(engine) as session:
        account = Account(
            id=str(uuid.uuid4()),
            name=json.name,
            image=json.image,
            goal=json.goal,
            password=json.password,
            classroomId=json.classroomId
        )
        session.add(account)
        session.commit()
        session.refresh(account)
        return account

def getAll():
    with Session(engine) as session:
        result = session.execute(select(Account)).mappings().all()
        print(result)
        return result

def get(id):
    with Session(engine) as session:
        query = (
            select(Account, func.sum(Transaction.value).label('sum'))
            .outerjoin(Account.transactions)
            .where(Account.id == id)
            .group_by(Account.id)
            .options(joinedload(Account.transactions))
        )
        result = session.execute(query).mappings().first()

        if result is None:
            raise HTTPException(status_code=404, detail="Não foi possível encontrar uma conta")
        if result.Account.transactions:
            for transaction in result.Account.transactions:
                transaction.day = transaction.day.strftime('%d/%m/%Y')

        return result

def patch():
    pass
