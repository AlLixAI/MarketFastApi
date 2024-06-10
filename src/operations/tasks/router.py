from fastapi import APIRouter, Depends

from src.auth.base_config import current_user
from src.operations.tasks.tasks import send_email_congrats_to_join

router = APIRouter(prefix="/emailsend")


# @router.get("/gratz_registation")
# async def gratz_registation(user=Depends(current_user)):
#     send_email_congrats_to_join.delay(user.username, user.email)
#     return {
#         "status": 200,
#         "data": "Письмо отправлено"
#     }