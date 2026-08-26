# Task 1:
# Copy Item model + items_db + next_id + the POST/GET endpoints from day03 into this file (reuse, don't reinvent)

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi import Request
from fastapi.responses import JSONResponse
app = FastAPI()
class Item(BaseModel):
    name: str
    price: float
    quantity :int
    in_stock: bool = True
items_db: dict[int, Item] = {}
next_id = 1

@app.post("/items" ,status_code=201)
def create_item(item: Item):
    global next_id
    items_db[next_id] = item
    response = {"id": next_id, "name": item.name, "price": item.price, "in_stock": item.in_stock}
    next_id += 1
    return response

@app.get("/items/{item_id}")
def get_item(item_id:int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

# Task 2:
# Create a custom exception class: InsufficientQuantityError
# - __init__ should store item_id, requested_qty, available_qty
# - Plain Python class, no FastAPI imports involved in this class at all

class InsufficientQuantityError(Exception):
    def __init__(self, item_id: int, requested_qty: int, available_qty: int):
        self.item_id = item_id
        self.requested_qty = requested_qty
        self.available_qty = available_qty


# Task 3:
# Add a `quantity: int` field to the Item model (represents stock count)
# Create endpoint POST /items/{item_id}/purchase
# - Query param: qty: int (how many the caller wants to buy)
# - Before writing code: predict what happens right now, with no custom handler registered yet, if you just `raise InsufficientQuantityError(...)` — what does the client actually receive? (hint: try it and see what an unhandled exception looks like)
# - If item_id not in items_db: raise HTTPException(404) as before
# - If qty > item.quantity: raise InsufficientQuantityError(item_id, qty, item.quantity)
# - Otherwise: subtract qty from item.quantity, return the updated item

# If you raise InsufficientQuantityError without a custom handler, the client will receive a 500 Internal Server Error response with a generic error message. The response will not include any specific details about the error, such as the item_id, requested_qty, or available_qty. This is because FastAPI does not know how to handle this custom exception by default, and it treats it as an unhandled exception.
@app.post("/items/{item_id}/purchase")
def purchase_item(item_id: int, qty: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    item = items_db[item_id]
    if qty > item.quantity:
        raise InsufficientQuantityError(item_id, qty, item.quantity)
    item.quantity -= qty
    return item

# Task 4:
# Register a global handler: @app.exception_handler(InsufficientQuantityError)
# - Return a JSONResponse with status_code=409
# - content should include: error type, item_id, requested_qty, available_qty
# - Re-test the same purchase-too-much request from Task 3 — compare the response to what you got before the handler existed

@app.exception_handler(InsufficientQuantityError)
def out_of_stock_handler(request: Request, exc: InsufficientQuantityError):
    return JSONResponse(
        status_code=409,
        content={"error": "out_of_stock", "item_id": exc.item_id, "requested_qty": exc.requested_qty, "available_qty": exc.available_qty}
    )

# Task 5:
# Test via /docs:
# - Purchase a valid quantity (should succeed, quantity decreases)
# - Purchase more than available quantity (should return your custom 409, not a raw 500)
# - Purchase from a nonexistent item_id (should still return the plain 404 from Task 3 — confirm HTTPException and your custom handler coexist without conflict)

# I tested the endpoints via /docs and confirmed the following behaviors:
# POST /items with a real body, e.g. {"name": "Pen", "price": 1.5, "quantity": 10, "in_stock": true} — the id I got back = 1
# POST /items/{that_id}/purchase?qty=3 —  status code : 200, body: {"name": "Pen", "price": 1.5, "quantity": 7, "in_stock": true}
# POST /items/{that_id}/purchase?qty=999  —  status: 409, body: {"error": "out_of_stock", "item_id": 1, "requested_qty": 999, "available_qty": 7}
# POST /items/999999/purchase?qty=1 — status: 404, body: {"detail": "Item not found"}