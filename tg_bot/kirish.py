from aiogram import Bot, Dispatcher, types
from aiogram import F
import asyncio
import pprint

BOT_TOKEN = "8154340985:AAH3eE46q4ud_Y9_LxY934jIrBbcc461W_g"

ADMIN_CHATID = 5547740249

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
valyutalar = {
    'usd': 11900,
    'rubl': 172
}

@dp.message()
async def send_messages(message):
    pprint.pprint(message.__dict__)
    await message.forward(chat_id=ADMIN_CHATID)

    if message.text == '/start':
        await message.answer(
            "Assalomu alaykum! 👋\n"
        )
    
    elif message.text == 'nima gap':
        await message.answer(
            "Tinchlik"
        )
    elif message.text.lower() in valyutalar.keys():
        await message.answer(
            f"{message.text} = {valyutalar[message.text.lower()]} so'm"
        )
    else:
        await message.forward(chat_id=message.chat.id)
    

async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


# polling 
# webhook