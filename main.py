
import os
from fastapi import APIRouter, FastAPI
from aiogram import Bot
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
USER_ID = os.getenv("USER_TG_ID")

if not BOT_TOKEN or not USER_ID:
    raise ValueError("BOT_TOKEN or USER_ID is not set")
user_id: int = int(USER_ID)


bot = Bot(token=BOT_TOKEN)
app = FastAPI(docs_url="/api/docs",
              redoc_url="/api/redoc",
              openapi_url="/api/openapi.json",
              swagger_ui_parameters={
                  "tryItOutEnabled": True,
              })

router = APIRouter()


@router.post("/api/")
async def telegram_webhook():
    await bot.send_message(user_id, "message")
    return {"message": "OK"}

app.include_router(router)
