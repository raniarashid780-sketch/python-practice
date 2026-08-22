# Task 1:
# Create endpoint GET /items/{item_id}
# - item_id parameter must be typed int (let FastAPI's validation handle bad input, don't hand-check it yourself)
# - Return a JSON object with item_id and its Python type (confirm via type(item_id).__name__)
# - Before writing code: predict in a comment what status code /items/abc (non-integer) returns, and why

from fastapi import FastAPI
app = FastAPI()

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return{"item_id": item_id, "item_id_type": type(item_id).__name__}


# Task 2:
# Create endpoint GET /search
# - Query param keyword: str, required (no default — must error if missing)
# - Query param max_results: int = 10 (has a default — optional)
# - Return both values received, plus a boolean flag: used_default (True if max_results wasn't provided)

@app.get("/search")
def search(keyword: str, max_results: int = 10):
    return {"keyword": keyword, "max_results": max_results, "used_default": max_results == 10}


# Task 3:
# Create endpoint GET /items/{item_id}/reviews
# - Path param: item_id: int (required, identifies the item)
# - Query param: min_rating: float = 0.0 (optional, filters reviews)
# - Return item_id and min_rating together in one JSON response
# - Before writing code: predict what happens if someone passes min_rating=abc — status code and why

@app.get("/items/{item_id}/reviews")
def get_item_reviews(item_id: int, min_rating: float = 0.0):
    return {"item_id": item_id, "min_rating": min_rating}
# Error occurs if min_rating=abc because FastAPI will try to convert the string "abc" to a float, which is not possible.
# This will result in a 422 Unprocessable Entity status code, indicating that the input data is invalid.

# Task 4:
# Hit all three endpoints via /docs (Swagger UI), not just curl
# - Confirm each shows correct types, correct required/optional marking
# - Screenshot or note anything /docs shows that surprises you — if nothing surprises you, look harder

# Swagger UI showed item_id as an integer path parameter. /items/5 returned status 200, while /items/abc returned status 422 because FastAPI rejected the non-integer value.