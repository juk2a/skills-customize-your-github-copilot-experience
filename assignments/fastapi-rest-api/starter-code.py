from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Book Catalog API")


class Book(BaseModel):
    title: str
    author: str
    publication_year: int


books: dict[int, Book] = {}
next_book_id = 1


@app.get("/health")
def health_check():
    # TODO: Return a JSON status message.
    pass


@app.get("/books")
def list_books():
    # TODO: Return all books in the catalog.
    pass


@app.post("/books")
def create_book(book: Book):
    # TODO: Assign a unique ID, store the book, and return it with its ID.
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Return the book or raise HTTPException with a 404 status code.
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    # TODO: Replace the book or raise HTTPException with a 404 status code.
    pass


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    # TODO: Delete the book or raise HTTPException with a 404 status code.
    pass
