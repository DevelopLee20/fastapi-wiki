import dataclasses

from app.documents.base_document import BaseDocument


@dataclasses.dataclass(kw_only=True, frozen=True)
class CheckDocument(BaseDocument):
    name: str
    value: int
