from fastapi import APIRouter

from app.services.check_service import CheckService
from app.responses.check_response import CheckResponse, CheckData

router = APIRouter()


@router.get("/db_check", response_model=CheckResponse)
async def root_page() -> CheckResponse:
    service_return = await CheckService.db_check_service()

    data = CheckData(check_docs_list=service_return)
    return CheckResponse(success=True, detail="데이터베이스 조회 성공", data=data)
