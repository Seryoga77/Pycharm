from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


api = "8186883981:AAH7QN1VmiOUmZbz2UOMVnF6pYuWe290pdE"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

button_calculate = KeyboardButton('Рассчитать')
button_info = KeyboardButton('Информация')

keyboard_markup = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_markup.add(button_calculate, button_info)


@dp.message_handler(commands=['start'])
async def cmd_start(message):
    await message.answer("Добро пожаловать! Выберите действие:", reply_markup=keyboard_markup)


@dp.message_handler(lambda message: message.text == 'Рассчитать', state='*')
async def set_age(message):
    await UserState.age.set()  # Устанавливаем состояние age
    await message.answer('Введите свой возраст:')


@dp.message_handler(state=UserState.age)
async def set_growth(message, state: FSMContext):
    await state.update_data(age=message.text)
    await UserState.growth.set()
    await message.answer('Введите свой рост:')


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state: FSMContext):
    await state.update_data(growth=message.text)
    await UserState.weight.set()
    await message.answer('Введите свой вес:')


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state: FSMContext):
    await state.update_data(weight=message.text)


    user_data = await state.get_data()
    age = user_data.get('age')
    growth = user_data.get('growth')
    weight = user_data.get('weight')

    bmr = 10 * weight + 6.25 * growth - 5 * age - 161
    await message.answer(f'Ваша норма калорий: {bmr:.2f} калорий в день.')

    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
