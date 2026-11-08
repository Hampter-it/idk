from sqlalchemy import URL, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from idk.settings import settings

database_url = URL.create(
    drivername="postgresql+psycopg",
    username=settings.POSTGRES_USER,
    password=settings.POSTGRES_PASSWORD,
    host="localhost",
    port=5432,
    database=settings.POSTGRES_DB,
)


engine = create_engine(database_url)
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass
