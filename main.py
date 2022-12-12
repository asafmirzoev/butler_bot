import os

from pyrogram import Client, filters, enums
from pyrogram.raw import functions, types

app = Client("butler_account", api_id=os.getenv('API_ID'), api_hash=os.getenv('API_HASH'))


async def chat_filter(self, user: Client, query):
    return query.chat.type == enums.ChatType.PRIVATE

static_data_filter = filters.create(chat_filter)

@app.on_message(static_data_filter)
async def hello(client: Client, message: filters.Message):
    me = await client.get_me()
    name = message.from_user.first_name if message.from_user.first_name != None else message.from_user.username
    if me.status != enums.UserStatus.ONLINE:
        await message.reply(f"Привет <b>{name}!👋</b>\nЯ <b><i>бот-дворецкий</i></b>🤖, рад с Вами познакомиться😃\nК сожалению, сейчас <b><u>не</u> в сети</b>❌.\nОн ответит вам как только войдет в сеть:) Спасибо за ожидание! <b>Хорошего дня!</b>", parse_mode=enums.ParseMode.HTML)
        await app.invoke(functions.account.UpdateStatus(offline=True))


app.run()