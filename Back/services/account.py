from .context import engine
from ..domain.account import Account
from ..domain.transaction import Transaction
from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import HTTPException
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
        query = select(Account).where(Account.id==id).join(Transaction)
        result = session.scalar(query)
        if(result==None):
            raise HTTPException(status_code=404, detail="Não foi possível encontrar uma conta")
        account = result.transactions
        return result

def patch():
    pass
