from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Mp3MqModel(Base):
    __tablename__ = 'h_mp3_mq'
    id = Column(Integer, primary_key=True)
    mp3_path = Column(String(255))
    type = Column(Integer)
