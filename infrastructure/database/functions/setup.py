from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker, AsyncSession

from infrastructure.database.models import BaseModel
from tgbot.config import DatabaseConfig


def create_engine(db: DatabaseConfig, echo: bool = False) -> AsyncEngine:
    """ Create a new async engine instance. """
    engine = create_async_engine(
        url=db.construct_sqlalchemy_url(),
        echo=echo
    )
    return engine


def create_session_pool(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    """ Create a session pool bound to the specified engine. """
    session_pool = async_sessionmaker(
        bind=engine,
        expire_on_commit=False
    )
    return session_pool


async def sync_database_tables(engine: AsyncEngine, metadata: MetaData = BaseModel.metadata, drop_tables: bool = False):
    """
    Synchronize database tables with the models defined in the metadata.

    If `drop_tables` is True, it drops existing tables before creating new ones.
    """
    async with engine.begin() as connection:
        # Synchronization tables
        if drop_tables:
            await connection.run_sync(metadata.drop_all)  # Drop all defined tables
        await connection.run_sync(metadata.create_all)  # Create all defined tables
