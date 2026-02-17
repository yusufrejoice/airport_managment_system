from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


AIRPORT_DATABASE_URL = "postgresql://postgres:postgres123@localhost/AIRPORT"


engine = create_engine(AIRPORT_DATABASE_URL)

SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base=declarative_base()