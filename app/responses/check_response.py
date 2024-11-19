from pydantic import BaseModel

from app.responses.base_response import BaseApiResponse


class CheckDocs(BaseModel):
    id: str
    name: str
    value: int


class CheckData(BaseModel):
    check_docs_list: list[CheckDocs]


class CheckResponse(BaseApiResponse):
    data: CheckData
