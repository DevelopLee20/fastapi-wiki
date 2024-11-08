from fastapi import APIRouter

root_router = APIRouter()


@root_router.get("/")
async def root_page():
    return {"I'm ready."}
