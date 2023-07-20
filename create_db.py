#importing the Base class and engine from the database file
from database import Base ,engine

print("Creating Databsae .....")

#creatig the databse using the metadata and base 
Base.metadata.create_all(engine)
