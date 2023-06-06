from dataclasses import dataclass

from environs import Env
from sqlalchemy import URL


@dataclass
class DatabaseConfig:
    host: str  # Database server host. Local example: 127.0.0.1 or localhost
    user: str  # Database user name
    password: str  # Database user password
    database: str  # Database name
    port: int = 5432  # Database port. Default value: 5432

    def construct_sqlalchemy_url(self) -> URL:
        return URL.create(
            drivername='postgresql+asyncpg',  # Using the asyncpg driver
            username=self.user,
            password=self.password,
            database=self.database,
            host=self.host,
            port=self.port
        )


@dataclass
class TelegramBot:
    token: str  # Telegram bot token
    admin_ids: list[int]  # List of bot admins


@dataclass
class Miscellaneous:
    other_params: str = None  # Your other params


@dataclass
class Config:
    tg_bot: TelegramBot
    db: DatabaseConfig
    misc: Miscellaneous


def load_config(path: str = None) -> Config:
    env = Env()
    env.read_env(path)  # If the path is not specified, it is equal to .env

    return Config(
        tg_bot=TelegramBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS")))
        ),
        db=DatabaseConfig(
            user=env.str("DATABASE_USER"),
            password=env.str("DATABASE_PASSWORD"),
            database=env.str("DATABASE_NAME"),
            host=env.str("DATABASE_HOST"),
            port=env.int("DATABASE_PORT", 5432)
        ),
        misc=Miscellaneous()
    )
