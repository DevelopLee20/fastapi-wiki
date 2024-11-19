from app.db.check_collection import CheckCollection
from app.responses.check_response import CheckDocs


class CheckService:
    @classmethod
    async def db_check_service(cls) -> list[CheckDocs]:
        result = await CheckCollection.select_all()

        new_result = []
        for res in result:
            new_result.append(
                CheckDocs(id=str(res._id), name=res.name, value=res.value)
            )

        return new_result
