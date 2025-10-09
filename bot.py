from aiogram import Bot, Dispatcher, types, F
import asyncio
from keyboards import menu_btn
from states import PsixologState, DasturchiState,DietologState,TeacherState
from aiogram.fsm.context import FSMContext
import requests
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
# from aiogram.utils.markdown import escape_md

bot = Bot(token="7488234070:AAEuySI239tTrke60wznY_n2BBNYIsx8_xo",default=DefaultBotProperties(
        parse_mode=None
    ))
dp = Dispatcher()

GEMINI_API_KEY = "AIzaSyBzz3oxpnhO2ii67d4vU0BEEeI1AidRcu0"

@dp.message(F.text=='/start')
async def start(message: types.Message, state:FSMContext):
    await state.clear()
    await message.answer("Assalamu alaykum!\nAI yordamchi botimizga xush kelibsiz\nO'zingiznga kerakli mutahasisni tanlang", reply_markup=menu_btn)


async def connect_ai(prompt):
    try:
        from google import genai

        client = genai.Client(api_key="AIzaSyDpZNMY3YFLf78N8tq-6c29DRIypXk6_6A")

        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=prompt)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Gemini API xatosi: {e}")
        return e

@dp.message(F.text=='Psixolog')
async def start(message: types.Message, state:FSMContext):
    await state.clear()
    await message.answer("Iltimos Psixologga nima savolingiz bo'lsa batafsil yozib yuboring.")
    await state.set_state(PsixologState.prompt)

@dp.message(F.text=='Dietolog')
async def start(message: types.Message, state:FSMContext):
    await state.clear()
    await message.answer("Iltimos Dietologga nima savolingiz bo'lsa batafsil yozib yuboring.")
    await state.set_state(DietologState.prompt)


@dp.message(PsixologState.prompt)
async def echo(message: types.Message):
    text = message.text

    prompt = F"""
    Salom sen o'zingni huddi 15 yillik tajribga ega kuchli psixologiya fanlari doktori sifatida meni quyidagi savolimga javob yoz. Iltimos javobdagi so'zlar soni 300-400 tadan oshmasin!

    {text}
    """
    response = await connect_ai(prompt)
    # safe_response = escape_md(response)
    await message.answer(response)



@dp.message(DietologState.prompt)
async def echo(message: types.Message):
    text = message.text

    prompt = F"""
    Salom sen o'zingni huddi 15 yillik tajribga ega kuchli dietologiya fanlari doktori sifatida meni quyidagi savolimga javob yoz. Iltimos javobdagi so'zlar soni 300 tadan oshmasin!

    {text}
    """
    response = await connect_ai(prompt)
    # safe_response = escape_md(response)
    await message.answer(response)
    print(response)
    # await message.answer(response)
    

async def main():
    print("Bot is start...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

