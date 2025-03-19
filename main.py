from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Здорова, брат! Я бот. Как сам?")


def handle_messages(update: Updater, context: CallbackContext) -> None:
    text = update.message.text
    update.message.reply_text(f"Вы сказали: {text}")


def main():
    updater = Updater('7610498247:AAH2yMoqcU1Ap02w3haMBrEGEkvBDyoSXM0')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text & ~
                   Filters.command, handle_messages))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
