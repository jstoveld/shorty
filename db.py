from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASEURL = "mysql+pymysql://user:password@localhost/shortydb"

engine = create_engine(DATABASEURL)
SessionLocal = sessionmaker(autocommut=False, autoflush=False, bind=engine)
Base = declarative_base()