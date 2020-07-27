from typing import List
import logging
from fastapi import Depends, FastAPI, HTTPException, APIRouter
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
import json 
from starlette.requests import Request
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
api_router = APIRouter()
logger = logging.getLogger("api")


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()



@api_router.get("/notes/", response_model=List[schemas.Note])
def read_notes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_notes(db, skip=skip, limit=limit)


@api_router.post("/notes/", response_model=schemas.Note)
def create_note(
    note: schemas.NoteCreate, db: Session = Depends(get_db)
):
    return crud.create_note(db=db, note=note)

@api_router.put("/notes/{note_id}", response_model=schemas.Note)
def update_note(note_id: int, note: schemas.NoteCreate, db: Session = Depends(get_db)):
    note = crud.update_note(db=db, note_id=note_id, note=note)


@api_router.delete("/notes/{note_id}", response_model=schemas.Note)
def delete_note(note_id: int, db: Session = Depends(get_db)):
    crud.delete_note(db=db, note_id=note_id)


async def logmy200(request: Request):
    try:
        logger.debug(await request.json())
        logger.debug("Metoda " + request.method)
        logger.debug(request.url)
        logger.debug(request.query_params)
    except Exception as ex:
        logger.debug(ex)
        pass


app.include_router(api_router, dependencies=[Depends(logmy200)])

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8081",
    "http://localhost:4000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
