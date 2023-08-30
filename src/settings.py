import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(os.getenv('DATABASE_URL'))
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()


def get_session(func):
    def wrapper(*args, **kwargs):
        session = Session()
        func(session=session, *args, **kwargs)
        session.commit()
        session.close()
    return wrapper
