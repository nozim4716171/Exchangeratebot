import requests
from aiogram import Bot,Dispatcher,executor,types
import datetime

API_KEY="afff1a78fcb6779e4e7b563e"
API_TOKEN="5481424034:AAFidoyD5N7eSTIovAora9KWxpc7XDjXH8A"

bot=Bot(API_TOKEN)
db=Dispatcher(bot)

vaqt=datetime.datetime.now()

@db.message_handler(commands=["start"])
async def start(message: types.Message):
    currency="USD"
    url=f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"
    response = requests.get(url)
    fullname=message.from_user.full_name
    natija=response.json()['conversion_rate']
    await message.answer(f"Assalomu aleykum {fullname}. Bugungi {vaqt} holatga ko'ra 1 USD {natija} so'mga teng.")
    
    
    
    
if __name__ == '__main__':
    executor.start_polling(db)








