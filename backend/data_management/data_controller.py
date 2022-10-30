from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from sqlalchemy.orm.session import Session

from . import model as mdl

import common.schemas as schemas


SQLALCHEMY_DATABASE_URL = "sqlite:///db.sqlite"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

@contextmanager
def session_context():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()



def create_standing(standing_schema:schemas.Standing):
    with session_context() as session:
        standing = mdl.Standing()

        for pos_schema in standing_schema.positions:
            pos = mdl.Position(**pos_schema.dict())
            session.add(pos)
            standing.positions.append(pos)

        session.add(standing)
        session.commit()
    return standing_schema.json()
