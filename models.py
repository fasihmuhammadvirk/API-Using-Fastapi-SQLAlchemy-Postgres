#importing the base from the database file that our model will inherit 
from database import Base
#importing the Column, String, Integer and Boolean entities to use in our table
from sqlalchemy import Column,String,Integer,Boolean


#creating the Items class that will be converted into our database table
class Items(Base):
    
    #table name that will be in the database 
    __tablename__ = "items"
    
    
    ### coulmn that will be in our database ###
    
    id = Column(Integer(),primary_key=True) #id will store integer  that is also our primary key 
    name = Column(String(45),nullable=False) #column that will contain name and it canot be null, is a string 
    description = Column(String(255),nullable=False) #cannot be null and for description, will be a string 
    price = Column(Integer(),nullable=False ) #cannot be null is integer and for price 
    on_offer = Column(Boolean(),default=False) #a boolean type column that will store if in offer or not defualt value is False
    
    #creating a method for our model class Items when called will return a dictionay of all column values
    def to_dict(self):
        
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description' : self.description,
            'on offer': self.on_offer
        }
    
    #it will be called whenever an object of this class printed
    def __repr__(self):
        return f"<Item { self.name } Pirce {self.price}>"
