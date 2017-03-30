from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AlarmModel(Base):
    __tablename__ = 'h_alarm'
    id = Column(Integer, primary_key=True)
    time = Column(String(255))
    path = Column(String(255))
    create_time = Column(DateTime)
