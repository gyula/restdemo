#!/usr/bin/env python

from sqlalchemy import Column, Integer, String, DateTime, func, create_engine
from sqlalchemy.ext.declarative import declarative_base
from dotenv import Dotenv
Base = declarative_base()

class Repo(Base):
    __tablename__ = 'repos'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    creator = Column(String(255))
    access_cnt = Column(Integer, default=0)
    creation_date = Column(DateTime, default=func.now())

if __name__ == "__main__":
    try:
        env = Dotenv('./env')
        engine = create_engine(env['DB_URI'])
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
    except IOError:
        env = os.environ

