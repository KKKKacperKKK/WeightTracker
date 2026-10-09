import os
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

url = os.environ["DATABASE_URL"]

engine = create_engine(url)
SessionLocal = sessionmaker(engine)

class Base(DeclarativeBase):
    pass


