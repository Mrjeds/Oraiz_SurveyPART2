from sqlmodel import Field , SQLModel
import hashlib

class Users(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    password: str


class book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    Name: str
    Price: float
    Note: str
