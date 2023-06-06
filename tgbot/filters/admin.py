from typing import Union

from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery

from tgbot.config import Config


class AdminFilter(BaseFilter):
    """ Filter that checks if a user is an admin. """
    is_admin: bool = True

    async def __call__(
            self,
            obj: Union[Message, CallbackQuery],
            config: Config
    ) -> bool:
        # Checks whether the user sending the message or callback query is an admin.
        return (obj.from_user.id in config.tg_bot.admin_ids) == self.is_admin
