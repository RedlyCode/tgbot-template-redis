import datetime

from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class BaseModel(DeclarativeBase):
    """ Basic model for creating tables. """
    pass


class TimedBaseModel(BaseModel):
    """
    Timed base model for creating tables.

    This class adds 2 new columns to tables created with it:
    ::
        created_at — the date the record was created in the database.
        updated_at — the date the record data was last modified in the database.

    """
    __abstract__ = True

    created_at: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.utcnow,
        server_default=func.now()
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        server_default=func.now()
    )
