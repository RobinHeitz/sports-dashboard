from sqlalchemy.orm.session import Session
from sqlalchemy.orm import sessionmaker, scoped_session
import sqlalchemy as db
from sqlalchemy.exc import InvalidRequestError, ResourceClosedError

from contextlib import contextmanager

import traceback
import threading
from typing import List, Tuple, Set

# session = None
def create_database(db_name = "db.sqlite"):
    engine_str = f"sqlite:///{db_name}"
    engine = db.create_engine(engine_str, connect_args={'check_same_thread':False},)
    connection = engine.connect()
    # metadata = db.MetaData()
    factory = sessionmaker(bind=engine, expire_on_commit=False)
    return scoped_session(factory)

def create_session() -> Session:
    return SessionCreate()

SessionCreate = create_database()



#Alternative: Using context-manager
@contextmanager
def session_context():
    session = create_session()
    try:
        yield session
    finally:
      session.close()


def catch_exceptions(f):
    
    def _log_e(f, e):
        logger.error(f"Exception occured while doing db operations: {f.__name__}.")
        logger.error(traceback.format_exc())

    
    def wrap(*args, **kwargs):
        try:
            logger.info(f"--- {f.__name__}() called")
           
            session_obj = create_session()
           
            return_val = f(session_obj, *args, **kwargs)
            # session_obj.close()
            return return_val

        except Exception as e:
            _log_e(f,e)
        
        finally:
            session_obj.close()

    return wrap



#####################
###  Transmission ###
#####################

@catch_exceptions
def create_transmission(session:Session, config:TransmissionConfiguration) -> Transmission:
    if config == None:
        raise ValueError("Config shouldn't be None if Transmission gets created.")

    t = Transmission(transmission_configuration = config)
    session.add(t)

    for step in AssemblyStep:
        a = Assembly(transmission = t, assembly_step = step)
        session.add(a)

    session.commit()
    return t

