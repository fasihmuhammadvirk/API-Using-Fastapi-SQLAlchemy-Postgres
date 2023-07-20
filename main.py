#importing the FastAPI to create apis and status to check their status and HTTPException to handle exception 
from fastapi import FastAPI, status, HTTPException

#importing the BaseModel for validating the data 
from pydantic import BaseModel

#importing session to query our database 
from database import session

#to return the list type 
from typing import List

#importing our model 
import models


#creating the app for making apis 
app = FastAPI()

# creating a model using pydantic
class Item(BaseModel):

    id: int
    name: str
    description: str
    price: int
    on_offer: bool

    class Config:
        orm_mode = True


# creating the session for doing operation on the database
db = session()


# creating the get response to get all the data from the database
@app.get("/items", response_model=List[Item],status_code= status.HTTP_200_OK)
def get_all_items():
    items = db.query(models.Items).all()
    return items

# creating the get response  to get an item by specific id from the database
@app.get('/items/{item_id}', response_model=Item, status_code=status.HTTP_200_OK)
def get_an_item(item_id: int):
    an_item = db.query(models.Items).filter(models.Items.id == item_id).first()
    
    if an_item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    
    return an_item


# creating the post response to add/create an item in the database
@app.post('/items', response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: Item):

    db_item = db.query(models.Items).filter(models.Items.name == item.name).first()
    if db_item is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Item Already Exits")

    new_item = models.Items(
        id=item.id,
        name=item.name,
        description=item.description,
        price=item.price,
        on_offer=item.on_offer
    )
    

    db.add(new_item)
    db.commit()


    return new_item

# creating a put response to update an item in the database
@app.put('/item/{item_id}', response_model=Item, status_code=status.HTTP_200_OK)
def update_item(item_id: int, item: Item):

    item_to_update = db.query(models.Items).filter(models.Items.id == item_id).first()
    
    if item_to_update is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")    
    item_to_update.name = item.name
    item_to_update.description = item.description
    item_to_update.price = item.price
    item_to_update.on_offer = item.on_offer

    db.commit()

    return item_to_update


# creating a delete response to delete the an item from the database
@app.delete('/item/{item_id}', response_model=Item, status_code=status.HTTP_200_OK)
def delete_item(item_id: int):

    item_to_delete = db.query(models.Items).filter(
        models.Items.id == item_id).first()

    if item_to_delete is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Resource Not Found")

    db.delete(item_to_delete)
    db.commit()

    return item_to_delete
