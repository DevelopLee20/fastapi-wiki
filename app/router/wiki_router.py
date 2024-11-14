from fastapi import APIRouter, Response
from app.utils.template_util import templates

wiki_router = APIRouter()


@wiki_router.get("/wiki")
async def wiki_main_page():
    return templates.TemplateResponse("index.html", {"request": {}})
