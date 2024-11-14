from fastapi import FastAPI, Response
from sqlalchemy import create_engine
from fastapi.staticfiles import StaticFiles

from app.core.settings import settings
from app.router.common_router import common_router
from app.router.wiki_router import wiki_router

app = FastAPI()

# 라우터
app.include_router(common_router)
app.include_router(wiki_router)

# 마운트
app.mount("/static", StaticFiles(directory="app/static"), name="static")
