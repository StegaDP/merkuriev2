import enum

from db.user import get_user_posibilities
from utils import messages


async def connection_approved(mode, message) -> bool:
    idx = message.chat.id
    data = get_user_posibilities(idx)
    if (mode == ConnectionMode.create and data[0]) or (mode == ConnectionMode.approve and data[1]) or \
            (mode == ConnectionMode.pay and data[2]):
        return True
    await message.answer(messages.NOT_APPROVED)
    return False


class ConnectionMode(enum.Enum):
    create = 'can_create'
    approve = 'can_approve'
    pay = 'can_pay'
