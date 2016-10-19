import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from dotenv import Dotenv

try:
    env = Dotenv('./env')
    Session = sessionmaker(autocommit=False,
                           autoflush=False,
                           bind=create_engine(env['DB_URI']))
    session = scoped_session(Session)
except IOError:
    env = os.environ
