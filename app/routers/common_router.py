from fastapi import APIRouter, Response

router = APIRouter()


@router.get("/")
async def root_page() -> dict[str, str]:
    return {"Are you Ready?": "I'm ready."}


@router.get("/favicon.ico")
async def favicon() -> Response:
    return Response(content="", media_type="image/x-icon")
