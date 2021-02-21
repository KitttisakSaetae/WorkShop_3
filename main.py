from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field
from starlette.responses import JSONResponse
from typing import Dict, Optional, List, Tuple
import uvicorn

app = FastAPI()


@app.get("/")
def index():
    return JSONResponse(content={"message": "Hello,  World"}, status_code=200)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=3000, reload=True)


# EXAMPLE path param
@app.get("/profile/{name}")
def get_path_parameter(name: str):
    return JSONResponse(
        content={"message": f"My name is : {name}"},
        status_code=200,
    )


# EXAMPLE query param
@app.get("/profile/{name}")
def get_query_parameter(start: int = 0, limit: int = 0):
    return JSONResponse(
        content={"message": f"Profile start : {start}, limit : {limit}"},
        status_code=200,
    )


# EXAMPLE list of book 1
@app.get("/books")
def get_book():
    dict_books = [
        {
            "book_id": 1,
            "book_name": "Harry Potter and Philosopher's stone",
            "page": 223,
        },
        {
            "book_id": 2,
            "book_name": "Harry Potter and the Chamber of Secrets",
            "page": 251,
        },
        {
            "book_id": 3,
            "book_name": "Harry Potter and the Prisoner of Azkaban",
            "page": 251,
        },
    ]
    return JSONResponse(content={"status": "ok", "data": dict_books}, status_code=200)


# EXAMPLE list of book
@app.get("/books")
def get_books_by_id(book_id: int):
    book = {
        "book_id": 1,
        "book_name": "Harry Potter and Philosopher's stone",
        "page": 223,
    }
    responses = {"status": "ok", "data": "book"}
    return JSONResponse(content=responses, status_code=200)


# EXAMPLE create endpoint 1
class createBookPayload(BaseModel):
    id: str
    name: str
    page: int


# EXAMPLE create endpoint 2
@app.post("/books")
def create_books(rep_body: createBookPayload):
    rep_body_dict = rep_body.dict()
    id = rep_body_dict["id"]
    name = rep_body_dict["name"]
    page = rep_body_dict["page"]
    book = {
        "id": id,
        "name": name,
        "page": page,
    }
    responses = {"status": "ok", "data": "book"}
    return JSONResponse(content=responses, status_code=201)


# EXAMPLE update endpoint 1
class updateBookPaylord(BaseModel):
    name: str
    page: int


# EXAMPLE update endpoint 2
@app.patch("/books/{book_id}")
def update_book_by_id(rep_body: updateBookPaylord, book_id: str):
    rep_body_dict = rep_body.dict()

    name = rep_body_dict["name"]
    page = rep_body_dict["page"]

    print(f"name: {name}, page: {page}")

    update_message = f"Update book id {book_id} is complete !!"
    responses = {"status": "ok", "data": update_message}
    return JSONResponse(content=responses, status_code=200)


# EXAMPLE delete endpoint
@app.delete("/books/{book_id}")
def delete_book_by_id(book_id: int):
    delete_message = f"Delete book id {book_id} is COMPLETE  !!"
    responses = {"status": "ok", "data": delete_message}
    return JSONResponse(content=responses, status_code=200)