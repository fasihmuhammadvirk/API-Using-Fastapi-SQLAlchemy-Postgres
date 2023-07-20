from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


#creating a model using pydantic
class Item(BaseModel):
    
    id:int 
    name:str 
    description:str 
    price:int
    on_offer:bool 

#this only return the simple jason response 
@app.get("/")
def root():
    return {"message": "Hello World"}


#giving item id as query parameter
@app.put("/items/{item_id}")
def update_items(item_id:int,item:Item):
    #returing the data from the model 
    return{
        
        'name':item.name,
        'description' : item.description,
        'price' : item.price,
        'on_offer' : item.on_offer
        
    }
    
#to give data we have to provide it in its body 
#like this 
'''
{
"id":1,
"name":"milk",
"description":"1 litre milk ",
"price":2000,
"on_offer":true
}

'''
    
    

    
