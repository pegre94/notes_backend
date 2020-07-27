from typing import List
from pydantic import BaseModel


class NoteBase(BaseModel):
    name: str = None
    content: str = None
    creationDate: str
    creationTime: str
    editionDate: str
    editionTime: str
    public: bool

class NoteCreate(NoteBase):
    pass

class Note(NoteBase):
    id: str

    class Config:
        orm_mode = True
