from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy_utils import database_exists, create_database
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy import select


from ..domain.base import Base
from ..domain.account import Account
from ..domain.classroom import Classroom
from ..domain.transaction import Transaction

engine = None

def get_engine(user, password, host, port, db):
    global engine
    if engine==None:
        url = f"postgresql://{user}:{password}@{host}/{db}"
        if not database_exists(url):
            create_database(url)
        engine = create_engine(url, pool_size=50, echo=False)
    return engine

engine = get_engine("postgres", "cocota", "localhost", 5432, "tesste")
Base.metadata.create_all(engine)

