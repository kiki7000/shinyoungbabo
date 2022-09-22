from odmantic import AIOEngine
from odmantic.query import QueryExpression
from motor.motor_asyncio import AsyncIOMotorClient

from typing import Union, Optional, List

from AssacCore.models.dataclass.config import Config

from AssacCore.models.database.user import DUser

from AssacCore.data.jobs import JobList


class AssacCore:
    config: Config
    db: AsyncIOMotorClient
    engine: AIOEngine

    def __init__(self, config: Config):
        self.config = config
        self.connect_database()

    def connect_database(self):
        self.db = AsyncIOMotorClient(self.config.dbURL)
        self.engine = AIOEngine(self.db, "assaccream")

    # Users

    async def user_register(self, discord_id: int) -> Optional[DUser]:
        check_exists = await self.engine.count(DUser, DUser.discordID == discord_id)
        if check_exists:
            return None

        user = DUser(discordID=discord_id, job=JobList.choice().name)

        await self.engine.save(user)
        return user

    async def get_users(
        self,
        *queries: Union[QueryExpression, dict, bool],
        sort: Optional[None] = None,
        skip: int = 0,
        limit: Optional[int] = None
    ) -> List[DUser]:
        res = await self.engine.find(DUser, *queries, sort=sort, skip=skip, limit=limit)
        return res

    async def get_user(self, discord_id: int) -> Optional[DUser]:
        res = await self.engine.find_one(DUser, DUser.discordID == discord_id)
        return res
