from fastapi import APIRouter, Depends, HTTPException
from app.services import get_db
from schema import Classes, Sessions, Question, Answer
from . import models
from sqlalchemy.orm import Session
from datetime import datetime

app = APIRouter()


@app.post("/class")
def create_class(class_: Classes, db: Session = Depends(get_db)):
    db_class = models.Classes(
        class_name = class_.class_name,
    )


@app.get("/all_classes/")
def all_classes():
    pass


@app.get("/class/{class_id}")
def view_class(class_id):
    pass
