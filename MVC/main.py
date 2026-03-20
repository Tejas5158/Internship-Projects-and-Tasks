from fastapi import FastAPI
from database.db import Base, engine
from routes.user_routes import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)