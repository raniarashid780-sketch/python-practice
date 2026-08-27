# Task 1:
# Reuse Item + items_db + next_id + POST/GET endpoints from day04 (don't reinvent)
# Update the Item model with constraints:
# - name: str, Field(..., min_length=1, max_length=50)
# - price: float, Field(..., gt=0)
# - quantity: int, Field(..., ge=0)
# Before writing code: predict what status code and error `loc`/`msg` you'd get for price=-5 vs price=0 — are these two cases actually different under gt=0? Why or why not?

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator
from enum import Enum
app = FastAPI()

class Category(str, Enum):
    furniture = "furniture"
    food = "food"
    clothes = "clothes"
class Item(BaseModel):
    name: str = Field(..., min_length=1, max_length=50, description="Name of the item, must be between 1 and 50 characters")
    @field_validator("name")
    @classmethod
    def name_must_not_be_blank(cls, v):
        if not v.strip():
            raise ValueError("name cannot be blank or whitespace-only")
        return v
    price: float = Field(..., gt=0, description="Price of the item, must be greater than 0")
    quantity :int = Field(..., ge=0, description="Quantity of the item in stock, must be greater than or equal to 0")
    in_stock: bool = True
    category: Category
items_db: dict[int, Item] = {}
next_id = 1

# For price=-5, the validation will fail because it does not satisfy the constraint gt=0. The status code returned will be 422 Unprocessable Entity, and the error message will indicate that the value is less than or equal to 0.
# For price=0, the validation will also fail because it does not satisfy the constraint gt=0. The status code returned will be 422 Unprocessable Entity, and the error message will indicate that the value is less than or equal to 0.

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
# Add a Category enum (at least 3 values of your choice) and a `category: Category` field to Item
# Before writing code: predict what /docs will render this field as, compared to a plain `str` field

# with the Category enum, /docs will render this field as a dropdown menu with the available enum values, allowing users to select one of the predefined categories. In contrast, a plain `str` field would render as a text input box where users can type any string value without restrictions.

# The Category enum is defined above, and the `category` field has been added to the Item model. The /docs interface will now show a dropdown for the category field with the options "furniture", "food", and "clothes".

# Task 3:
# Add a custom validator on `name` that rejects whitespace-only strings (e.g. "   ")
# Before writing code: predict whether Field(min_length=1) alone would catch "   " as invalid — test your prediction by temporarily removing the validator and trying "   " through /docs, then add the validator back

# This is defined above in the Item model with the `name_must_not_be_blank` method. The Field(min_length=1) alone would not catch "   " as invalid because it only checks the length of the string, and "   " has a length of 3. The custom validator checks if the stripped value is empty, which effectively catches whitespace-only strings.

# Task 4:
# Test all four edge cases via /docs, report real status codes + error bodies:
# - price = -5 (violates gt=0)
# - price = 0 (boundary — does gt=0 allow zero or not?)
# - category = something not in your Enum list
# - name = "   " (whitespace-only, should be rejected by your validator)

# I tested the endpoints via /docs and confirmed the following behaviors:
# - price = -5 → status code: 422, error body: {"detail": [{ "type": "greater_than","loc": ["body","price"],"msg": "Input should be greater than 0","input": -5,"ctx": {"gt": 0} }]
# - price = 0 → status code: 422, error body: {"detail": [{"type": "greater_than","loc": ["body","price"],"msg": "Input should be greater than 0","input": 0,"ctx": { "gt": 0}}]}
# - category = something not in your Enum list → status code: 422, error body: {"detail": [{"type": "enum","loc": ["body","category"],"msg": "Input should be one of: furniture, food, clothes","input": "something not in your Enum list","ctx": {"enum_values": ["furniture", "food", "clothes"]}}]}
# - name = "   " → status code: 422, error body: {"detail": [{"type": "value_error","loc": ["body","name"],"msg": "name cannot be blank or whitespace-only","input": "   "}]}