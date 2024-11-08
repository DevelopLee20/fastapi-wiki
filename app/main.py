from fastapi import FastAPI
from sqlalchemy import create_engine

from app.core.settings import settings
from app.router.root_page import root_router

app = FastAPI()

app.include_router(root_router)
