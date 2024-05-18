from aiogram.enums import ParseMode
from aiogram.types import URLInputFile

from aiogram.filters import Command
from aiogram import types, F, Router
from db import Database

router = Router()
db = Database('DB')

amount = 0
#id_users = []
markup = types.ReplyKeyboardRemove()
ending_markup = types.ReplyKeyboardRemove()

@router.message(Command(commands=["start"]))
async def cmd_start(message: types.Message):
    image_from_url=URLInputFile("https://static.tildacdn.com/tild3537-6661-4639-a235-393535656431/logo-zoo.png")
    await message.answer_photo(image_from_url, caption="В Московском зоопарке пару месяцев будет ремонт,\
                поэтому некоторых животных расселяют по квартирам,\
                если Ты ответственный человек\
                пройди тест, узнай кого бы Ты мог забрать!? 😃")

    kb = [[types.KeyboardButton(text="Начнем!")]]
    keyboard_start = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="СМЕЛЕЙ!")
    await message.answer("Подумай и ...", reply_markup=keyboard_start)


@router.message(Command(commands=["info"]))
async def cmd_info(message: types.Message):
    kb = [[types.KeyboardButton(text="Начнем!")]]
    keyboard_start = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    image_from_url = URLInputFile("https://static.tildacdn.com/tild3537-6661-4639-a235-393535656431/logo-zoo.png")
    await message.answer_photo(image_from_url, caption="В Московском зоопарке пару месяцев будет ремонт,\
                    поэтому некоторых животных расселяют по квартирам,\
                    если Ты ответственный человек\
                    пройди тест, узнай кого бы Ты мог забрать!? 😃 Жми 'Начнем!'", reply_markup=keyboard_start)


@router.message(F.text.lower() == "начнем!")
async def yours_choice(message: types.Message):
    if not db.user_exist(message.from_user.id):
        db.add_user(message.from_user.id)
        kb0 = [
            [types.KeyboardButton(text="Зима")],
            [types.KeyboardButton(text="Лето")]
        ]
        keyboard0 = types.ReplyKeyboardMarkup(keyboard=kb0,
        resize_keyboard=True,
        input_field_placeholder="Синхронизируйся со своим питомцем")
        await message.answer("Какое время года Вы предпочитаете?", reply_markup=keyboard0)
    else:
        await message.answer("Ваш питомец Вами уже выбран, этого не отменить", reply_markup=ending_markup)


@router.message(F.text.lower() == "зима")
async def yours_choice(message: types.Message):
    global amount
    amount += 3
    kb1 = [
        [types.KeyboardButton(text="Ночь")],
        [types.KeyboardButton(text="День")]
    ]
    keyboard1 = types.ReplyKeyboardMarkup(keyboard=kb1,
    resize_keyboard=True,
    input_field_placeholder="Синхронизируйся со своим питомцем")
    await message.answer("Какое время суток Вы предпочитаете?", reply_markup=keyboard1)

@router.message(F.text.lower() == "лето")
async def yours_choice(message: types.Message):
    global amount
    amount += 1
    kb1 = [
        [types.KeyboardButton(text="Ночь")],
        [types.KeyboardButton(text="День")]
    ]
    keyboard1 = types.ReplyKeyboardMarkup(keyboard=kb1,
    resize_keyboard=True,
    input_field_placeholder="Синхронизируйся со своим питомцем")
    await message.answer("Какое время суток Вы предпочитаете?", reply_markup=keyboard1)

@router.message(F.text.lower() == "ночь")
async def yours_choice(message: types.Message):
    global amount
    amount += 6
    kb2 = [
        [types.KeyboardButton(text="Фрукты")],
        [types.KeyboardButton(text="Сосиска в тесте")]
    ]
    keyboard2 = types.ReplyKeyboardMarkup(keyboard=kb2,
    resize_keyboard=True, input_field_placeholder="Помните, что Ваш питомец совсем не против совместной трапезы")
    await message.answer("Чтобы Вы сейчас съели?", reply_markup=keyboard2)

@router.message(F.text.lower() == "день")
async def yours_choice(message: types.Message):
    global amount
    amount += 5
    kb2 = [
    [types.KeyboardButton(text="Фрукты")],
    [types.KeyboardButton(text="Сосиска в тесте")]
    ]
    keyboard2 = types.ReplyKeyboardMarkup(keyboard=kb2,
    resize_keyboard=True, input_field_placeholder="Помните, что Ваш питомец совсем не против совместной трапезы")
    await message.answer("Чтобы Вы сейчас съели?", reply_markup=keyboard2)

@router.message(F.text.lower() == "фрукты")
async def yours_choice(message: types.Message):
    #file_ids = []
    global amount
    amount += 7
    if amount == 13:
        image_from_url = URLInputFile(
            "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/79da8af4-7f66-45fc-b526-2d2395ebc9a8.jpeg")
        await message.answer_photo(
            image_from_url,
            caption="Вам очень подойдет ЛЕМУР КОШАЧИЙ, возьмите его 😃", reply_markup=markup
        )

        amount = 0
        await message.answer("ЭТО СУДЬБА!", reply_markup=ending_markup)
    elif amount == 14:
        image_from_url = URLInputFile(
            "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/11563396-1d63-4451-a0e6-a3fd4282d5cf.jpeg")
        await message.answer_photo(
            image_from_url,
            caption="Вам очень подойдет ДВУХЦВЕТНЫЙ КОЖАН, возьмите его 😃", reply_markup=markup
        )
        amount = 0
        await message.answer("ЭТО СУДЬБА!", reply_markup=ending_markup)
    elif amount == 15:
        image_from_url = URLInputFile(
            "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/132e290b-76fd-4fc1-a70c-eba12dcc9e1c.jpeg")
        await message.answer_photo(
            image_from_url,
            caption="Вам очень подойдет КАПСКАЯ ЗЕМЛЯНАЯ БЕЛКА, возьмите его 😃", reply_markup=markup

        )
        amount = 0
        await message.answer("ЭТО СУДЬБА!", reply_markup=ending_markup)
    elif amount == 16:
        image_from_url = URLInputFile(
            "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/29c253e7-449f-4f6e-b2ab-e8f89b3f71c2.jpeg")
        await message.answer_photo(
            image_from_url,
            caption="Вам очень подойдет БОРОДАТАЯ НЕЯСЫТЬ, возьмите его 😃", reply_markup=markup

        )
        amount = 0
        await message.answer("ЭТО СУДЬБА!", reply_markup=ending_markup)
    else:
        if amount == 17:
            image_from_url = URLInputFile(
                "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/29c253e7-449f-4f6e-b2ab-e8f89b3f71c2.jpeg")
            await message.answer_photo(
                image_from_url,
                caption="Вам очень подойдет БЕЛАЯ СОВА, возьмите его 😃", reply_markup=markup

            )
            amount = 0
            await message.answer("ЭТО СУДЬБА!", reply_markup=ending_markup)
@router.message(F.text.lower() == "сосиска в тесте")
async def yours_choice(message: types.Message):
    file_ids = []
    global amount
    amount += 8
    if amount == 13:
        image_from_url = URLInputFile(
            "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/79da8af4-7f66-45fc-b526-2d2395ebc9a8.jpeg")
        await message.answer_photo(
            image_from_url,
            caption="Вам очень подойдет ЛЕМУР КОШАЧИЙ, возьмите его 😃", reply_markup=markup

        )
        amount = 0
        await message.answer("ЭТО СУДЬБА!", reply_markup=ending_markup)
    elif amount == 14:
        image_from_url = URLInputFile(
            "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/11563396-1d63-4451-a0e6-a3fd4282d5cf.jpeg")
        await message.answer_photo(
            image_from_url,
            caption="Вам очень подойдет ДВУХЦВЕТНЫЙ КОЖАН, возьмите его 😃", reply_markup=markup

        )
        amount = 0
        await message.answer("ЭТО СУДЬБА!", reply_markup=ending_markup)
    elif amount == 15:
        image_from_url = URLInputFile(
            "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/132e290b-76fd-4fc1-a70c-eba12dcc9e1c.jpeg")
        await message.answer_photo(
            image_from_url,
            caption="Вам очень подойдет КАПСКАЯ ЗЕМЛЯНАЯ БЕЛКА, возьмите его 😃", reply_markup=markup

        )
        amount = 0
        await message.answer("ЭТО СУДЬБА!", reply_markup=ending_markup)
    elif amount == 16:
        image_from_url = URLInputFile(
            "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/29c253e7-449f-4f6e-b2ab-e8f89b3f71c2.jpeg")
        await message.answer_photo(
            image_from_url,
            caption="Вам очень подойдет БОРОДАТАЯ НЕЯСЫТЬ, возьмите его 😃", reply_markup=markup

        )
        amount = 0
        await message.answer("ЭТО СУДЬБА!", reply_markup=ending_markup)
    elif amount == 17:
        image_from_url = URLInputFile(
            "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/042d7c00-9abf-4553-9b3d-eedd08f72090.jpeg")
        await message.answer_photo(
            image_from_url,
            caption="Вам очень подойдет БЕЛАЯ СОВА, возьмите его 😃", reply_markup=markup

        )
        amount = 0
        await message.answer("ЭТО СУДЬБА!", reply_markup=ending_markup)
    else:
        await message.answer("У нас нет для Вас питомца")
        amount = 0
        await message.answer("ЭТО СУДЬБА!", reply_markup=ending_markup)