"""Signacula DB and API"""

import datetime
from sqlmodel import Field, SQLModel


class Bookmark(SQLModel, table=True):
    """A bookmarked URL"""
    id: int | None = Field(default=None, primary_key=True)
    url: str
    title: str | None = None
    backend: str | None = None
    frequency: int | None = None
    favicon: str | None = None  # TODO a URL??
    description: str | None = None
    image: str | None = None  # TODO a URL??
    site_name: str | None = None
    rating: float | None = None


class Tag(SQLModel, table=True):
    """A tag on a bookmark"""
    id: int | None = Field(default=None, primary_key=True)
    tag: str
    bookmark_id: int = Field(foreign_key="bookmark.id")

class Action(SQLModel, table=True):
    """A record taken of an action on a bookmark"""
    id: int | None = Field(default=None, primary_key=True)
    bookmark_id: int = Field(foreign_key="bookmark.id")
    action_type: str | None = None  # TODO archive, spider, review, develop
    started: datetime.datetime | None = None
    completed: datetime.datetime | None = None
    error: str | None
    result: str | None
