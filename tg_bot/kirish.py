from aiogram import Bot, Dispatcher
import asyncio
import pprint
import requests

BOT_TOKEN = "8154340985:AAH3eE46q4ud_Y9_LxY934jIrBbcc461W_g"
ADMIN_CHATID = 5547740249

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
valyutalar = {
    'usd': 11900,
    'rubl': 172
}
# Weather condition to emoji mapping
weather_icons = {
    "01d": "☀️",  # Clear sky
    "01n": "🌙",  # Clear sky night
    "02d": "⛅",  # Few clouds
    "02n": "🌥️",  # Few clouds night
    "03d": "☁️",  # Scattered clouds
    "03n": "☁️",  # Scattered clouds night
    "04d": "☁️",  # Broken clouds
    "04n": "☁️",  # Broken clouds night
    "09d": "🌧️",  # Shower rain
    "09n": "🌧️",  # Shower rain night
    "10d": "🌦️",  # Rain
    "10n": "🌦️",  # Rain night
    "11d": "⛈️",  # Thunderstorm
    "11n": "⛈️",  # Thunderstorm night
    "13d": "❄️",  # Snow
    "13n": "❄️",  # Snow night
    "50d": "🌫️",  # Mist
    "50n": "🌫️",  # Mist night
}

OPENWEATHER_API_KEY = "f96032cd8d3260d7ba30e35f4376829b"
async def weather(city) -> None:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric&lang=uz"

    response = requests.get(url)
    data = response.json()
    return data


@dp.message()
async def send_messages(message):
    # pprint.pprint(message.__dict__)

    if message.text == '/start':
        await message.answer(
            "Assalomu alaykum! 👋\n"
            "/w City - Shahar ob-havo ma'lumotlarini ko'rish!"
        )
    
    elif message.text == 'nima gap':
        await message.answer(
            "Tinchlik"
        )
    elif message.text.startswith('/w '):
        city = message.text.split(' ')[1]
        data = await weather(city)
        print(data['cod'])
        if data['cod'] == 200:
            temp = data['main']['temp']
            max_temp = data['main']['temp_max']
            min_temp = data['main']['temp_min']

            icon_code = data['weather'][0]['icon']
            weather_emoji = weather_icons.get(icon_code, "🌥️")

            info = (
                f"Shahar: {city.title()} {weather_emoji}\n\n"
                f"🌡️ Hozirgi harorat: {temp} ℃\n"
                f"🔥 Eng yuqori harorat: {max_temp} ℃\n"
                f"❄️ Eng past harorat: {min_temp} ℃"
            )
            print(f"\n\n{city} shahridagi ob-havo ma'lumotlari:\n")
            await message.answer(info)
        else:
            await message.answer("⚠️ Kechirasiz, bunday shahar topilmadi!")
    

async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    # data = asyncio.run(weather('tokio'))
    # temp = data['main']['temp']
    # max_temp = data['main']['temp_max']
    # min_temp = data['main']['temp_min']

    # info = f"Harorat: {temp} ℃\n" \
    #         f"Yuqori harorat: {max_temp} ℃\n" \
    #         f"Past harorat: {min_temp} ℃"
    
    # print(info)


# polling 
# webhook