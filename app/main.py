from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routers import check_router, common_router, wiki_router

app = FastAPI()

# 라우터
app.include_router(check_router.router)
app.include_router(common_router.router)
app.include_router(wiki_router.router)

# 마운트
app.mount("/static", StaticFiles(directory="app/static"), name="static")
