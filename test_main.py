from fastapi.testclient import TestClient
from fastapi import status 
from database import session
from models import Items
import json  


db = session()

from main import app 

client = TestClient(app)


### get all item test cases ###

def test_get_all_items():
    response = client.get('/items')
    
    items = db.query(Items).all()
    item_json = [json.dumps(item.to_dict()) for item in items]
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == len(item_json)
    
def test_get_no_item():
    response = client.get('/items')
    
    items = db.query(Items).all()
    assert response.status_code == status.HTTP_200_OK
    if items is None:
        assert response.json() == []

def test_return_none(): #this test should fail 
    response = client.get('/items')
    
    items = db.query(Items).all()
    assert response.status_code == status.HTTP_200_OK
    if items is not None:
        assert response.json == None 
    
def test_return_emptylst_while_populated(): #this test should fail
    response = client.get('/items')
    
    items = db.query(Items).all()
    assert response.status_code == status.HTTP_200_OK
    if items is not None:
        assert response.json == []
    

### to get an item ### 

def test_get_an_item():
    
    item_id = 2 
    response = client.get(f'/items/{item_id}')
    assert response.status_code == status.HTTP_200_OK
    item_data = response.json()
    assert 'id' in item_data
    items = db.query(Items).filter(Items.id == item_id).first()
    assert item_data['name'] == items.name
    assert item_data['description'] == items.description
    assert item_data['price'] == items.price
    assert item_data['on_offer'] == items.on_offer
    

def test_no_item_found():
    item_id = 2 
    response = client.get(f'/items/{item_id}')
    items = db.query(Items).filter(Items.id == item_id).first()
    if items is None:
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json() == { "detail": "Item not found" }

def test_return_no_item_found(): # this test should fail
    item_id = 2 
    response = client.get(f'/items/{item_id}')
    items = db.query(Items).filter(Items.id == item_id).first()
    if items is not None:
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json() == { "detail": "Item not found" }
        

### insert item test case ###

def test_insert_item():
    data = dict( 
        {
        "id": 0,
        "name": "string",
        "description": "string",
        "price": 0,
        "on_offer": True 
        }
                )
    
    response = client.post('/items',json=data)
    db_item = db.query(Items).filter(Items.id == data['id']).first()
    if db_item is None:
        
        assert response.status_code == status.HTTP_201_CREATED
    
        res_data = response.json()
        
        assert 'id' in res_data
        assert res_data['id'] == data['id']
        assert res_data['name'] == data['name']
        assert res_data['description'] == data['description']
        assert res_data['price'] == data['price']    

def test_item_already_in_db():
    data = dict( 
        {
        "id": 0,
        "name": "string",
        "description": "string",
        "price": 0,
        "on_offer": True 
        }
                )
    
    response = client.post('/items',json=data)

    db_item = db.query(Items).filter(Items.id == data['id']).first()
    
    if db_item is not None:
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json() == { "detail": "Item Already Exits" }
        

def test_no_body_provide():
    
    response = client.post('/items',json=None)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    

def test_insert_item_return_none(): #this test should fail 
    data = dict( 
        {
        "id": 10,
        "name": "ssstring",
        "description": "ssstring",
        "price": 110,
        "on_offer": True 
        }
                )
    
    response = client.post('/items',json=data)
    
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == { "detail": "Item Already Exits" }
    
    
### update item test case ###

def test_update_item_not_found():
    
    item_id = 10
    item_to_update = dict(    
                    {
        "id":10,
        "name": "ssstring",
        "description": "ssstring",
        "price": 110,
        "on_offer": True 
                    }
                            )
    response = client.put(f'/item/{item_id}',json = item_to_update)
    
    item_in_db = db.query(Items).filter(Items.id == item_id).first()
    
    if item_in_db is None:
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json() == {"detail":"Item not found"}
        

def test_update_item():
    
    item_id = 2
    item_to_update = dict(    
                    {
        "id":2,
        "name": "ssstring",
        "description": "ssstring",
        "price": 110,
        "on_offer": True 
                    }
                        )
    
    response = client.put(f'/item/{item_id}',json = item_to_update)
    item_in_db = db.query(Items).filter(Items.id == item_id).first()
    
    if item_in_db:
        res_data = response.json()
        assert response.status_code == status.HTTP_200_OK
        assert 'id' in res_data
        assert item_id == res_data['id'] 
        assert item_to_update['name'] == res_data['name']
        assert item_to_update['description'] == res_data['description'] 
        assert item_to_update['price'] == res_data['price'] 
        

def test_not_updating_item():
    
    item_id = 2
    item_to_update = dict(    
                    {
        "id":2,
        "name": "ssstring",
        "description": "ssstring",
        "price": 110,
        "on_offer": True 
                    }
                        )
    
    response = client.put(f'/item/{item_id}',json = item_to_update)
    item_in_db = db.query(Items).filter(Items.id == item_id).first()
    
    if item_in_db:
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json() == {"detail":"Item not found"}
        
### delete item test cases ###

def test_delete_item_not_found():
    
    item_id = 11
    response = client.delete(f'/item/{item_id}')
    
    item_to_delete = db.query(Items).filter(Items.id == item_id).first()
    
    if item_to_delete is None:
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json() == {"detail":"Resource Not Found"}
        

def test_not_deleting_item():#this test should fail 
        
    item_id = 11
    response = client.delete(f'/item/{item_id}')
    
    item_to_delete = db.query(Items).filter(Items.id == item_id).first()
    
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail":"Resource Not Found"}
    

def test_delete_item():
    
    item_id = 11
    response = client.delete(f'/item/{item_id}')
    
    item_to_delete = db.query(Items).filter(Items.id == item_id).first()


    assert response.status_code == status.HTTP_200_OK
    res_data = response.json()
        
    assert 'id' in res_data
    assert res_data['id'] == item_to_delete['id']
    assert res_data['name'] == item_to_delete['name']
    