from fastapi import APIRouter
from app.utils.template_util import templates
from typing import Any

router = APIRouter()


@router.get("/wiki")
async def wiki_main_page() -> Any:
    return templates.TemplateResponse("index.html", {"request": {}})
