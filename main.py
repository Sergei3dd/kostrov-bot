from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# ВСТАВЛЕННЫЙ ТОКЕН
TOKEN = "7745106864:AAG_AsieQt9P0vReBnKAO20BoEkAgNzmYRA"

def start(update, context):
    keyboard = [
        ["Силовая", "Масса и набор"],
        ["Кардио и выносливость", "Функциональная"],
        ["Растяжка и восстановление"]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text(
        "Здравствуйте!\n\n"
        "Добро пожаловать на платформу **KOSTROV LAB** — ваш личный помощник в тренировках.\n"
        "Выберите тип тренировки ниже 👇",
        reply_markup=reply_markup
    )

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
