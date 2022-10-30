from sqlalchemy import Integer, String, ForeignKey, Table, Enum, DateTime, Boolean, Column
from sqlalchemy.orm import relationship, backref, session
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Competition(Base):
    __tablename__ = "competition"
    id = Column(Integer, primary_key = True)
    

class Standing(Base):
    __tablename__ = "standing"
    id = Column(Integer, primary_key = True)
    positions = relationship("Position", backref=backref("standing"))
    
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)



class Position(Base):
    __tablename__ = "position"
    id = Column(Integer, primary_key = True)
    standing_id = Column(Integer, ForeignKey("standing.id"))

    position = Column(Integer)
    team = Column(String)
    played_games = Column(Integer)
    won = Column(Integer)
    draw = Column(Integer)
    lost = Column(Integer)
    points = Column(String)
    goal_difference = Column(Integer)
    goals_for = Column(Integer)
    goals_against = Column(Integer)
