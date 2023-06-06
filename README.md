**This [template](https://github.com/RedlyCode/tgbot-template) is used to develop [Telegram bots](https://core.telegram.org/bots/api) using
the [`aiogram v3.0+`](https://github.com/aiogram/aiogram/tree/dev-3.x) library.**

### This template was created using:

- [Python `3.11.3`](https://www.python.org/downloads/release/python-3113/)
- [Aiogram `3.0.0b8`](https://docs.aiogram.dev/en/dev-3.x/install.html)
- [SQLAlchemy `2.0.15`](https://docs.sqlalchemy.org/en/20/intro.html#installation)
- [asyncpg `0.27.0`](https://pypi.org/project/asyncpg/)
- [environs `9.5.0`](https://pypi.org/project/environs/)

### To start using:

1. Copy `.env.dist` to `.env` and fill in the required data.
2. Create and activate [venv](https://docs.python.org/3/library/venv.html).
3. Update python pip `python3 -m pip install --upgrade pip`.
4. Install dependencies from requirements.txt: `pip install -r requirements.txt`.
5. Run the project with the `python3 bot.py` command.

### How to make and register handlers:

1. Create the `you_name.py` module in the `handlers` folder.
2. Create a router in `you_name.py`.

```python
from aiogram import Router

user_router = Router()
```

You can make several [routers](https://docs.aiogram.dev/en/dev-3.x/dispatcher/router.html) in one module, and hang
handlers on each of them.
You can register handlers as decorators:

```python
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message):
    await message.reply("Greetings, regular user!")
```

Go to the `bot.py` file and add all the routers to it:

```python
from tgbot.handlers.admins.admin import admin_router
from tgbot.handlers.users.start import user_router

...


async def main():
    ...

    for router in [
        admin_router,
        user_router,
        ...
    ]:
        dp.include_router(router)
```
