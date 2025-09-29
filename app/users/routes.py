from fastapi import HTTPException, Depends, APIRouter
from app.users.schema import  UserCreate, UserOut, UserLogin
from app.services import get_db
from . import security, models
from sqlalchemy.orm import Session


app = APIRouter()


@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/register")
def register():
    pass


@app.post("/register", response_model=UserOut,)
def register(user: UserCreate, db: Session = Depends(get_db)):

    hashed_pw = security.hash_password(user.password)

    # checking if username or email isn't already taken
    if db.query(models.User).filter(models.User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username Already Taken")
    elif db.query(models.User).filter(models.User.email == user.email).first():
        raise HTTPException(status_code=400, detail="This Email Already has an Account")
    else:
        db_user = models.User(
            username = user.username, 
            firstname = user.firstname, 
            othernames = user.othernames,
            lastname = user.lastname, 
            email = user.email, 
            password = hashed_pw,
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

    return db_user


@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    if user.username:
        db_user = db.query(models.User).filter(models.User.username == user.username).first()
    elif user.email:
        db_user = db.query(models.User).filter(models.User.email == user.email).first()
    else:
        raise HTTPException(status_code=400, detail="Provice Necessary Credentials")
    
    if not db_user or not security.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid Credentials")
    db_user.password = None # this is supposed to remove the hashed pw. ??
    access_token = security.create_acces_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer", "user": db_user}


@app.get("/login")
def login():
    pass
