# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small book-catalog REST API with FastAPI. Practice defining endpoints, working with request and response data, and using HTTP status codes to handle common API operations.

## 📝 Tasks

### 🛠️ Create the API

#### Description
Set up the FastAPI application and add endpoints for checking that the API is running and listing the books in the catalog.

#### Requirements
Completed program should:

- Install FastAPI using `pip install "fastapi[standard]"`.
- Create a FastAPI application named `app` in `starter-code.py`.
- Provide a `GET /health` endpoint that returns a simple status message.
- Provide a `GET /books` endpoint that returns the current books as a JSON list.
- Run the app with `uvicorn starter-code:app --reload` and confirm the interactive API documentation is available at `/docs`.

### 🛠️ Add and Retrieve Books

#### Description
Define the data each book needs and let API clients add a book or retrieve one by its ID.

#### Requirements
Completed program should:

- Define a Pydantic model with a book's title, author, and publication year.
- Provide a `POST /books` endpoint that accepts a book and adds it to the catalog.
- Assign each new book a unique ID and include that ID in the response.
- Provide a `GET /books/{book_id}` endpoint that returns the requested book.
- Return an appropriate `404 Not Found` response when a requested book does not exist.

### 🛠️ Update and Remove Books

#### Description
Complete the catalog's basic CRUD operations by allowing clients to replace or remove a book.

#### Requirements
Completed program should:

- Provide a `PUT /books/{book_id}` endpoint that updates a book's details.
- Provide a `DELETE /books/{book_id}` endpoint that removes a book.
- Return an appropriate `404 Not Found` response when trying to update or delete a book that does not exist.
- Try each endpoint using the interactive documentation at `/docs` and confirm the responses are valid JSON.
