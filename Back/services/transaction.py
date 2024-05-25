from .context import engine
from ..domain.transaction import Transaction
from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import HTTPException
import uuid

def post(json):
    with Session(engine) as session:
        transaction = Transaction(
            id= str(uuid.uuid4()),
            origem=json.origem,
            valor=json.valor,
            accountId=json.accountId,
            dia=json.dia
        )
        session.add(transaction)
        session.commit()
        session.refresh(transaction)
        return transaction

def getAll():
    with Session(engine) as session:
        result = session.execute(select(Transaction)).mappings().all()
        return result

def get(id):
    with Session(engine) as session:
        query = select(Transaction).where(Transaction.id==id)
        result = session.scalar(query)
        if(result==None):
            raise HTTPException(status_code=404, detail="Não foi possível encontrar a transação")
        return result

def patch():
    pass
