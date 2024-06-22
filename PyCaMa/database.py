import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base


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
    from .car import Car
    Base.metadata.create_all(bind=engine)
