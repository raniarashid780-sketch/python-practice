# Task 1:
# Reuse Item, items_db, next_id from day05
# Create a dependency function get_item_or_404(item_id: int) -> Item that raises 404 or returns the item

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from fastapi import Request
app = FastAPI()
from fastapi import Depends

class Item(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    price: float = Field(..., gt=0)
    quantity: int = Field(..., ge=0)
    in_stock: bool = True

items_db: dict[int, Item] = {}
next_id = 1

def get_item_or_404(item_id: int) -> Item:
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]


# Task 2:
# Rewrite GET /items/{item_id} to use item: Item = Depends(get_item_or_404) instead of manual lookup
# Before writing: predict whether removing your old `if item_id not in items_db` check from inside the function will change the 404 behavior at all

# Removing the old `if item_id not in items_db` check from inside the function will not change the 404 behavior at all, because the dependency function `get_item_or_404` already handles the 404 error by raising an HTTPException if the item is not found. Therefore, the behavior will remain consistent, and a 404 status code will still be returned for invalid item IDs.
@app.get("/items/{item_id}")
def get_item(item: Item = Depends(get_item_or_404)):
    return item

@app.post("/items" ,status_code=201)
def create_item(item: Item):
    global next_id
    items_db[next_id] = item
    response = {"id": next_id, "name": item.name, "price": item.price, "in_stock": item.in_stock}
    next_id += 1
    return response

# Task 3:
# Rewrite POST /items/{item_id}/purchase (from day04/05 logic) to also use Depends(get_item_or_404) for fetching the item, keeping only the InsufficientQuantityError logic inline
class InsufficientQuantityError(Exception):
    def __init__(self, item_id: int, requested_qty: int, available_qty: int):
        self.item_id = item_id
        self.requested_qty = requested_qty
        self.available_qty = available_qty

@app.post("/items/{item_id}/purchase")
def purchase_item(item_id: int, quantity: int, item: Item = Depends(get_item_or_404)):
    if quantity > item.quantity:
        raise InsufficientQuantityError(item_id, quantity, item.quantity)
    item.quantity -= quantity
    return {"message": f"Purchased {quantity} of {item.name}. Remaining stock: {item.quantity}"}

@app.exception_handler(InsufficientQuantityError)
def out_of_stock_handler(request: Request, exc: InsufficientQuantityError):
    return JSONResponse(
        status_code=409,
        content={"error": "out_of_stock", "item_id": exc.item_id, "requested_qty": exc.requested_qty, "available_qty": exc.available_qty}
    )

# Task 4:
# Test via /docs: valid item_id, invalid item_id — confirm 404 still fires identically to before, report real status codes

# For /items/{item_id}
# Valid item_id: 200 OK, Response body: {"name": "furniture","price": 1,"quantity": 10,"in_stock": true}
# Invalid item_id: 404 Not Found, returns {"detail": "Item not found"}.

# For /items/{item_id}/purchase
# Valid item_id: 200 OK, Response body{"message": "Purchased 9 of furniture. Remaining stock: 1"}
# Invalid item_id: 409Error: Conflict, Response body{"error": "out_of_stock","item_id": 1,"requested_qty": 11,"available_qty": 1}