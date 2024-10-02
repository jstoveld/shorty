from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# FOR DEVELOPMENT
##VULNERABLE
DATABASEURL = "mysql+pymysql://admin:admin@localhost/shortydb"

engine = create_engine(DATABASEURL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()