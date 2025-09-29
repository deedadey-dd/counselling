from fastapi import FastAPI
from app import models, services
from app.users.routes import app as user_router
from app.school.routes import app as school_router

# create tables
models.Base.metadata.create_all(bind=services.engine)

app = FastAPI()

# include all routers from all other apps here
app.include_router(user_router)
app.include_router(school_router)
