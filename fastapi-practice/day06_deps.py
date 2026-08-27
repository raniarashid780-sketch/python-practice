# Task 1:
# Reuse Item, items_db, next_id from day05
# Create a dependency function get_item_or_404(item_id: int) -> Item that raises 404 or returns the item

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
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

# Task 3:
# Rewrite POST /items/{item_id}/purchase (from day04/05 logic) to also use Depends(get_item_or_404) for fetching the item, keeping only the InsufficientQuantityError logic inline

@app.post("/items/{item_id}/purchase")
def purchase_item(item_id: int, quantity: int, item: Item = Depends(get_item_or_404)):
    if quantity > item.quantity:
        raise HTTPException(status_code=400, detail="Insufficient quantity in stock")
    item.quantity -= quantity
    return {"message": f"Purchased {quantity} of {item.name}. Remaining stock: {item.quantity}"}

# Task 4:
# Test via /docs: valid item_id, invalid item_id — confirm 404 still fires identically to before, report real status codes

# Valid item_id: 200 OK, returns the item details.
# Invalid item_id: 404 Not Found, returns {"detail": "Item not found"}.