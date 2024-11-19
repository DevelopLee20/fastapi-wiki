from pydantic import BaseModel


class BaseApiResponse(BaseModel):
    success: bool
    detail: str
    data: BaseModel
