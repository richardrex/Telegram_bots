from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters

TG_TOKEN = '933914901:AAHrOvDD0XXekeVAXfh6RQYMK7dUZ-CHyFU'


def message_handler(bot: Bot, update: Update):
    user = update.effective_user
    if user:
        name = user.first_name
    else:
        name = 'nothing'
    text = update.effective_message.text
    reply_text = f'Hello, {name}!\n\n{text}'

    bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=reply_text,
    )


def main():
    bot = Bot(
        token=TG_TOKEN,
    )
    update = Updater(
        bot=bot,
    )

    handler = MessageHandler(Filters.all, message_handler)
    update.dispatcher.add_handler(handler)

    update.start_polling()
    update.idle()


if __name__ == '__main__':
    main()
