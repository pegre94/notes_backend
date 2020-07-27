from sqlalchemy.orm import Session
from sqlalchemy.dialects import sqlite
import models, schemas

def print_query(db, query):
    dialect = db.bind.dialect
    print(query.statement.compile(dialect=dialect))

def get_notes(db: Session, skip: int = 0, limit: int = 100):
    query = db.query(models.Note).offset(skip).limit(limit).all()
    # print(query.statement.compile(dialect=dialect))
    return query

def create_note(db: Session, note: schemas.NoteCreate):
    dialect = db.bind.dialect
    db_note = models.Note(**note.dict())
    db.add(db_note)
    # print_query(db, db.commit())
    db.commit()
    db.refresh(db_note)
    print(str(db_note))
    return db_note

def update_note(db: Session, note_id, note):
    matching_note = db.query(models.Note).filter_by(id=note_id).update(note)
    db.commit()
    return matching_note

def delete_note(db: Session, note_id):
    db.query(models.Note).filter_by(id=note_id).delete()
    db.commit()
