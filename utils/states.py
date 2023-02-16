from aiogram.dispatcher.filters.state import StatesGroup, State


class Admin(StatesGroup):
    edit = State()


class Report(StatesGroup):
    set_file = State()
    set_description = State()

