from fastapi import HTTPException, Depends, APIRouter
from schema import  UserCreate, UserOut
from app.services import get_db
from . import security, models
from sqlalchemy.orm import Session

app = APIRouter()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/register")
def register():
    pass


@app.post("/register", response_model=UserOut,)
def register(user: UserCreate, db: Session = Depends(get_db)):

    hashed_pw = security.hash_password(user.password)

    db_user = models.User(
        username = user.username, 
        firstname = user.firstname, 
        othernames = user.othernames,
        lastname = user.lastname, 
        email = user.email, 
        password = hashed_pw,
        class_id = user.class_id,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

@app.get("/login")
def login():
    pass


@app.post("/login")
def login():
    pass