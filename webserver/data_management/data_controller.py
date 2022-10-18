from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from sqlalchemy.orm.session import Session

# from ..schemas import Standing, Competition, Position

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


def get_something(db:Session, id:int):
    ...
    return id


def create_position(db:Session):
    with session_context() as session:
        ...
        #Do Some things