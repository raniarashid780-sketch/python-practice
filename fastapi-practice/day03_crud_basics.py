# Task 1:
# Redefine the Item model from Day 2 in this new file (name: str, price: float, in_stock: bool = True)
# Create an in-memory store: items_db: dict[int, Item] = {}
# Create a counter variable: next_id = 1

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True
items_db: dict[int, Item] = {}
next_id = 1

# Task 2:
# Create endpoint POST /items, status_code=201
# - Accept item: Item as request body
# - Store it in items_db using next_id as the key, then increment next_id
# - Return the stored item's id along with its fields

@app.post("/items" ,status_code=201)
def create_item(item: Item):
    global next_id
    items_db[next_id] = item
    response = {"id": next_id, "name": item.name, "price": item.price, "in_stock": item.in_stock}
    next_id += 1
    return response

# Task 3:
# Create endpoint GET /items/{item_id}
# - Before writing code: predict what happens if you just `return items_db.get(item_id)` for a nonexistent id, with no check — what status code, what body, and is that actually correct behavior for a "not found" case?
# - Implement it properly: raise HTTPException(status_code=404, detail="Item not found") if the id isn't in items_db, otherwise return the stored item

# If you just `return items_db.get(item_id)` for a nonexistent id, it would return `None` with a 200 OK status code. This is not correct behavior for a "not found" case, as it should return a 404 Not Found status code instead. Therefore, we need to check if the item exists and raise an HTTPException if it does not.
@app.get("/items/{item_id}")
def get_item(item_id:int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

# Task 4:
# Create endpoint PUT /items/{item_id}
# - Accept item: Item as the request body (a full replacement, not a partial update)
# - Before writing code: predict what should happen if item_id doesn't exist — should PUT create it, or 404? (there's a real, debatable answer here — decide and justify your choice in a comment)
# - Raise 404 if not found (or implement your justified alternative), otherwise overwrite items_db[item_id] entirely and return the updated item

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_id] = item
    return item



# Task 5:
# Create endpoint DELETE /items/{item_id}, status_code=204
# - Raise 404 if the id doesn't exist
# - Otherwise delete it from items_db and return nothing
# - Test via /docs: create an item (POST), fetch it (GET), delete it (DELETE), then GET it again — confirm the second GET returns 404

# I decided that if the item_id doesn't exist, the PUT request should return a 404 Not Found status code. This is because PUT is generally used for updating existing resources, and if the resource does not exist, it should indicate that the update cannot be performed. Creating a new resource with PUT could lead to confusion and unintended behavior, so it's better to enforce that the resource must exist before it can be updated.
@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return