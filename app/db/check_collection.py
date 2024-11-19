from typing import Any

from app.core.database import db
from app.documents.check_document import CheckDocument


class CheckCollection:
    _collection = db["check"]

    @classmethod
    def _parse(cls, check_dict: dict[str, Any]) -> CheckDocument:
        return CheckDocument(
            name=check_dict["name"],
            value=check_dict["value"],
        )

    @classmethod
    async def select_all(cls) -> list[CheckDocument]:
        result = []
        async for document in cls._collection.find(filter={}):
            result.append(cls._parse(document))

        return result
