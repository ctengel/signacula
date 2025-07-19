"""API for Bookmarks DB"""

from sqlmodel import SQLModel, Session, create_engine, select
from fastapi import FastAPI
from models import Bookmark, Action, Tag

DB_URL = "sqlite:///database.db"

connect_args = {"check_same_thread": False}
engine = create_engine(DB_URL, echo=True, connect_args=connect_args)


def create_db_and_tables():
    """Create all DB and tables"""
    SQLModel.metadata.create_all(engine)


app = FastAPI()


@app.on_event("startup")
def on_startup():
    """Function to setup DB on startup"""
    create_db_and_tables()

@app.post("/bookmarks/")
def create_bookmark(bookmark: Bookmark):
    """Submit a new bookmark"""
    with Session(engine) as session:
        session.add(bookmark)
        session.commit()
        session.refresh(bookmark)
        return bookmark



@app.get("/bookmarks/")
def read_bookmarks():
    """Return all bookmarks"""
    with Session(engine) as session:
        bookmark = session.exec(select(Bookmark)).all()
        return bookmark
