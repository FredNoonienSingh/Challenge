import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

from .car import Car

load_dotenv()
db_path = os.environ.get('SQLALCHEMY_DATABASE_URI')
engine = create_engine(db_path)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=True,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db() -> None:
    """
    initializes the db
    """
    Base.metadata.create_all(bind=engine)
