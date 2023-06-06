import logging

from aiogram import Bot

from tgbot.config import Config
from tgbot.services import broadcaster


async def on_startup_notify(bot: Bot) -> None:
    config: Config = bot.config

    await broadcaster.broadcast(
        bot=bot,
        users=config.tg_bot.admin_ids,
        text='The bot has been launched!',
        disable_notification=False
    )
    logging.info('The bot was launched successfully!')


async def on_shutdown_notify(bot: Bot) -> None:
    config: Config = bot.config

    await broadcaster.broadcast(
        bot=bot,
        users=config.tg_bot.admin_ids,
        text='The bot has been disabled!',
        disable_notification=False
    )
    logging.info('The bot has been disabled!')
