from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

class Database:
    def __init__(self, config: dict, echo: bool = False):
        self.config = config

        self.engine = create_async_engine(
            self._build_db_url(),
            echo=echo,
            pool_pre_ping=True,
        )

        self.SessionLocal = async_sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )

    def _build_db_url(self) -> str:
        return (
            f"postgresql+asyncpg://"
            f"{self.config['DB_USER']}:"
            f"{self.config['DB_PASSWORD']}@"
            f"{self.config['DB_HOST']}:"
            f"{self.config['DB_PORT']}/"
            f"{self.config['DB_NAME']}"
        )

    async def get_db(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.SessionLocal() as session:
            yield session