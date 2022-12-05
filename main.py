from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from telegram.ext.updater import Updater
import characters

updater = Updater("5757695495:AAEH8oZycKFRJqJXpq-8EoNyxjtx2I1Rtc0", use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hi there, this is GMK bot. "
                              "Here you can find info out about Mortal Kombat Characters."
                              "In case you dont know what to do use /help")


def help_message(update: Update, context: CallbackContext):
    update.message.reply_text("This bot provides info about MK characters."
                              "Here is the list of commands:\n"
                              "1./scorpion - info about Scorpion\n"
                              "2./subzero - info about Subzero\n"
                              "3./sonya - info about Sonya\n"
                              "4./johny - info about Johny\n"
                              "5./cassie - info about Cassie\n"
                              "4./kano - info about Kano\n"
                              "4./liukang - info about Liu Kang\n"
                              "4./kitana - info about Kitana")


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry I can't recognize you , you said '%s'" % update.message.text)


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help_message))

updater.dispatcher.add_handler(CommandHandler('scorpion', characters.scorpion))
updater.dispatcher.add_handler(CommandHandler('subzero', characters.subzero))
updater.dispatcher.add_handler(CommandHandler('sonya', characters.sonya))
updater.dispatcher.add_handler(CommandHandler('kano', characters.kano))
updater.dispatcher.add_handler(CommandHandler('cassie', characters.cassie))
updater.dispatcher.add_handler(CommandHandler('kitana', characters.kitana))
updater.dispatcher.add_handler(CommandHandler('liukang', characters.liukang))
updater.dispatcher.add_handler(CommandHandler('johny', characters.johny))

updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))


updater.start_polling()
