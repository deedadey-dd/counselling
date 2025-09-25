from fastapi import FastAPI
from . import models, services
from users.routes import router as user_router
from school.routes import router as school_router

# create tables
models.Base.metadata.create_all(bind=services.engine)

app = FastAPI()

# include all routers from all other apps here
app.include_router(user_router)
app.include_router(school_router)
