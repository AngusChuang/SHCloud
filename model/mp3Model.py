from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Mp3Model(Base):
    __tablename__ = 'h_mp3'
    id = Column(Integer, primary_key=True)
    mp3_path = Column(String(255))
    mp3_name = Column(String(255))
    mp3_name1 = Column(String(255))
    mp3_author = Column(String(255))
    create_time = Column(DateTime)
