import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '7184367883:AAFGU4g56xRXZimXqcePMkxS2LABiU5qOuU'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# @dp.message_handler(commands=['lang/uz'])
# async def change_lang(msg: types.Message):
#     wikipedia.set_lang('uz')
#     await msg.reply("O'zbek tiliga o'zgardi🇺🇿")


# @dp.message_handler(commands=['lang/ru'])
# async def change_lang2(msg: types.Message):
#     wikipedia.set_lang('ru')
#     await msg.reply("Rus tiliga o'zgardi🇷🇺")


# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
#     await message.reply("Assalomu Aleykum\nWico Botiga Xush kelibsiz!")
#     await message.answer("Nima haqida ma'lumot kerak?\nBitta so'z bilan ifodalang!\nNa'muna:\nToshkent\nTilni o'zgartirish uchun /lang/uz & /lang/ru")



# @dp.message_handler()
# async def sendInfo(message: types.Message):
#     try:
#         respond = wikipedia.summary(message.text)
#         await message.answer(respond)
#     except:
#         print("Ma'lumot topilmadi😔 ")


@dp.message_handler(commands=['start'])
async def start(message):
    await bot.send_message(message.from_user.id, message.text)

@dp.message_handler()
async def echo(message):
    await bot.send_message(message.from_user.id, message.text[::-1])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)