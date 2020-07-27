from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    content = Column(String, index=True)
    creationDate = Column(String, index=True)
    creationTime = Column(String, index=True)
    editionDate = Column(String, index=True)
    editionTime = Column(String, index=True)
    public = Column(Boolean, index=True)
