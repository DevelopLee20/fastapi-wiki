from fastapi import APIRouter, Response

common_router = APIRouter()


@common_router.get("/")
async def root_page():
    return {"I'm ready."}


@common_router.get("/favicon.ico")
async def favicon():
    return Response(content="", media_type="image/x-icon")
