from sqlalchemy import (Column, Integer, create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import settings


class Database(object):
    def __init__(self) -> None:
        self.engine = create_engine(f"sqlite:///{settings.DB_NAME}")
        self.connect_db()

    def connect_db(self) -> sessionmaker:
        Base.metadata.create_all(self.engine)
        session = sessionmaker(self.engine)
        return session()


Base = declarative_base()
database = Database()


class BaseDatabase(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
