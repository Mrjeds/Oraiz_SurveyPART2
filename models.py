from sqlmodel import Field , SQLModel
import hashlib

class survey(SQLModel, table=True):
    id: int|None = Field(default=None, primary_key=True)
    Name: str
    Age: int
    Birthday: str
    Gender: str
    Email: str
    SN: str
    Course: str
    YL: str
    Region: str
    Country:str



class Users(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    password: str
