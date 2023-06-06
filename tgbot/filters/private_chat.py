from typing import Union

from aiogram.enums import ChatType
from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery


class PrivateChatFilter(BaseFilter):
    """ Filter that checks if a chat is private. """
    is_private: bool = True

    async def __call__(
            self,
            obj: Union[Message, CallbackQuery]
    ) -> bool:
        # Checks whether the chat from the message or callback query is private.
        if isinstance(obj, CallbackQuery):
            obj = obj.message

        return (obj.chat.type == ChatType.PRIVATE) == self.is_private
