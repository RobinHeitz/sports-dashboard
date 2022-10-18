from sqlalchemy import Integer, String, ForeignKey, Table, Enum, DateTime, Boolean, Column
from sqlalchemy.orm import relationship, backref, session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Competition(Base):
    __tablename__ = "competition"
    id = Column(Integer, primary_key = True)
    

class Standing(Base):
    __tablename__ = "standing"
    id = Column(Integer, primary_key = True)
    positions = relationship("Position", backref=backref("standing"))


class Position(Base):
    __tablename__ = "position"
    id = Column(Integer, primary_key = True)
    standing_id = Column(Integer, ForeignKey("standing.id"))
