
#importing the declarative_base and sessionmaker 
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine


#url or connection string of our database 
database_url = 'postgresql://postgres:1213@localhost:5432/practice_database'

#create the engine for our database 
engine = create_engine(database_url,echo = True)

#creating the Base for our model class 
Base = declarative_base()

#creating the session to do query on database
session = sessionmaker(bind=engine)