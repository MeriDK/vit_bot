from datetime import datetime

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

from settings import TOKEN

# last bot's message
last_messages = {}


# check if last message has inline buttons
def check_last_message(update):
    last_message = last_messages.get(update.message.chat.id, None)
    try:
        last_message.edit_reply_markup()
    except:
        pass


def save_last_message(update, message):
    last_messages[update.message.chat.id] = message


# give button жми on /start command
def start(update, context):
    keyboard = [['жми']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text(text='hi', reply_markup=reply_markup)


# send message 🌝 with inline button Сменить
def push(update, context):
    check_last_message(update)

    keyboard = [[InlineKeyboardButton("Сменить", callback_data='change')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    msg = update.message.reply_text('🌝', reply_markup=reply_markup)

    save_last_message(update, msg)


# when Сменить is clicked change 🌝 on 🌚
def button(update, context):
    query = update.callback_query
    query.answer()
    msg = query.edit_message_text(text="🌚")


def main():
    updater = Updater(TOKEN, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))

    updater.dispatcher.add_handler(MessageHandler(Filters.text('жми'), push))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
