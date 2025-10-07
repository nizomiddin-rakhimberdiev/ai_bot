from aiogram.fsm.state import State, StatesGroup

class PsixologState(StatesGroup):
    prompt = State()

class DietologState(StatesGroup):
    prompt = State()

class DasturchiState(StatesGroup):
    prompt = State()

class TeacherState(StatesGroup):
    prompt = State()