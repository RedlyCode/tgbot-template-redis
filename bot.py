import asyncio
import logging

from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from infrastructure.database.functions.setup import create_engine, sync_database_tables, create_session_pool
from tgbot.config import Config, load_config
from tgbot.middlewares import ConfigMiddleware, DatabaseMiddleware
from tgbot.misc.functions import on_startup_notify, on_shutdown_notify

logger = logging.getLogger(__name__)


def register_global_middlewares(dp: Dispatcher, config: Config, session_pool):
    """ Function to register global middlewares for the bot. """
    dp.update.outer_middleware(ConfigMiddleware(config))
    dp.update.outer_middleware(DatabaseMiddleware(session_pool))


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s'
    )
    logger.info('Starting bot...')

    config = load_config('.env')  # Load the configuration from .env file
    storage = MemoryStorage()
    bot = Bot(token=config.tg_bot.token, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=storage)

    engine = create_engine(db=config.db, echo=True)
    await sync_database_tables(engine=engine, drop_tables=True)
    session_pool = create_session_pool(engine=engine)

    bot.config = config  # Binding the bot config to the bot object
    bot.db = session_pool  # Binding the session pool of the bot to the bot object

    # Registering bot routers
    for router in [
        ...  # Your routers
    ]:
        dp.include_router(router)

    # Registering bot middlewares
    register_global_middlewares(dp=dp, config=config, session_pool=session_pool)

    # Register the startup and shutdown notifications
    dp.startup.register(on_startup_notify)
    dp.shutdown.register(on_shutdown_notify)

    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt or SystemExit:
        logger.error('The bot has been disabled!')
