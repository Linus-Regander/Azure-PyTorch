from sqlalchemy.ext.asyncio import (create_async_engine, AsyncSession, async_sessionmaker)

from sqlalchemy.orm import DeclarativeBase

import os

class Database():
    def __init__(self, config, echo):
        self.config = config
        self.echo = echo
        self.engine = create_async_engine(
            self._build_db_url(),
            echo=self.echo,
        )
        self.SessionLocal = async_sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )
        
    def _build_db_url(self):
        return f"postgresql+asyncpg://{self.config['DB_USER']}:{self.config['DB_PASSWORD']}@{self.config['DB_HOST']}:{self.config['DB_PORT']}/{self.config['DB_NAME']}"

    async def get_db(self):
        async with self.SessionLocal() as session:
            yield session

class Base(DeclarativeBase):
    pass