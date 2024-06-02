from .context import engine
from ..domain.classroom import Classroom
from ..domain.account import Account
from ..domain.transaction import Transaction
from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import HTTPException
from sqlalchemy.orm import joinedload
import json
import uuid

def post(json):
    with Session(engine) as session:
        classroom = Classroom(
            id=str(uuid.uuid4())[:6].upper(),
            name=json.name,
            image=json.image
        )
        session.add(classroom)
        session.commit()
        session.refresh(classroom)
        return classroom

def getAll():
    with Session(engine) as session:
        result = session.execute(select(Classroom)).mappings().all()
        return result

def get(code):
    with Session(engine) as session:
        query = select(Classroom).where(Classroom.id==code).options(joinedload(Classroom.accounts))
        result = session.scalar(query)
        if(result==None):
            raise HTTPException(status_code=404, detail="Não foi possível encontrar uma sala")
        account = result.accounts
        return result

def patch():
    pass
