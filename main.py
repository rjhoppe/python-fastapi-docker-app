import os
import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from dotenv import load_dotenv

from models import Author
from models import Author as ModelAuthor
from models import Book
from models import Book as ModelBook
from schema import Book as SchemaBook
from schema import Author as SchemaAuthor

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

@app.get("/")
async def root():
  return("message:" "Hello World")

@app.post("/add-book/", response_model=SchemaBook)
def add_book(book: SchemaBook):
  db_book = ModelBook(title=book.title, rating=book.rating, author_id=book.author_id)
  db.session.add(db_book)
  db.session.commit()
  return db_book

@app.post("/add-author/", response_model=SchemaAuthor)
def add_book(author: SchemaAuthor):
  db_author = ModelAuthor(name=author.name, age=author.age)
  db.session.add(db_author)
  db.session.commit()
  return db_author

@app.get("/books/")
def get_books():
  books = db.session.query(Book).all()
  return books

# To run the server locally
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)