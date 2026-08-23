# Task 1:
# Create a Pydantic model `Item` with fields:
# - name: str (required)
# - price: float (required)
# - in_stock: bool = True (optional, default True)
# Before writing it: predict in a comment what happens if a client POSTs a body missing "price" entirely — status code, and what info (if any) the error tells you about which field failed

# If a client POSTs a body missing "price" entirely, the server will return a 422 Unprocessable Entity status code. The error message will indicate that the "price" field is missing and is required.
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True


# Task 2:
# Create endpoint POST /items
# - Accept `item: Item` as the request body (not a query/path param)
# - Return the item's name, price, and in_stock as a JSON object, accessed via dot notation (item.name, not item["name"])

app = FastAPI()
# @app.post("/items")
# def create_item(item :Item):
#     return {"Item name": item.name, "Price":item.price, "FastAPI default in_stock":item.in_stock}

# Task 3:
# Create a second model `ItemOut` with only name and price (no in_stock)
# - Apply it to POST /items via response_model=ItemOut
# - Before writing code: predict what the response body will contain when your function still returns the full `item` object (with in_stock) but response_model=ItemOut is set

# The response body will only contain the fields defined in the `ItemOut` model, which are `name` and `price`. The `in_stock` field will be filtered out and not included in the response, even though it is present in the returned `item` object.
class ItemOut(BaseModel):
    name: str
    price: float

@app.post("/items", response_model=ItemOut)
def create_item(item: Item):
    return item

# Task 4:
# Hit POST /items via /docs (Swagger UI)
# - Submit a full valid body, confirm response only shows name + price (in_stock filtered out)
# - Submit a body missing "price", confirm your Task 1 prediction against what /docs actually shows
# - Note one thing /docs's "Schema" tab shows for a Pydantic model that it didn't show for Day 1's simple int/str/float query params