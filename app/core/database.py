from motor.motor_asyncio import AsyncIOMotorClient
from app.core.settings import settings

# MongoDB 클라이언트 설정
client = AsyncIOMotorClient(settings.DATABASE_URL)  # MongoDB 연결 URL
database = client.get_database()  # 기본 DB에 연결

# 필요한 MongoDB 컬렉션을 가져옵니다
collection = database["base"]
