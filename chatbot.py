from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

import os
# import configparser
import logging
import redis

global redis1

def main():
    # Load your token and create an Updater for your Bot
    
    # config = configparser.ConfigParser()
    # config.read('config.ini')
    updater = Updater(token=(os.environ['ACCESS_TOKEN']), use_context=True)
    dispatcher = updater.dispatcher

    global redis1
    redis1 = redis.Redis(host=(os.environ['HOST']), password=(os.environ['PASSWORD']), port=(os.environ['REDISPORT']))

    # You can set this logging module, so you will know when and why things do not work as expected
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    
    # register a dispatcher to handle message: here we register an echo dispatcher
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("add", add))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("hello", hello_command))
    dispatcher.add_handler(CommandHandler("diet", diet_command))
    dispatcher.add_handler(CommandHandler("weight", weight_command))
    dispatcher.add_handler(CommandHandler("gym", gym_command))

    # To start the bot:
    updater.start_polling()
    updater.idle()


def echo(update, context):
    reply_message = update.message.text.upper()
    logging.info("Update: " + str(update))
    logging.info("context: " + str(context))
    context.bot.send_message(chat_id=update.effective_chat.id, text= reply_message)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Helping you helping you.')

def hello_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /hello is issued."""
    update.message.reply_text('Good day, Kevin!')

def diet_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /diet is issued."""
    update.message.reply_text('eat more Vegetable')

def weight_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /weight is issued."""
    update.message.reply_text('Track and field: 450 calories per half hour. It can exercise the whole body.
    Basketball: 250 calories per half hour. It can enhance flexibility and strengthen cardiopulmonary function.
    Bicycle: it consumes 330 calories every half hour. It's good for heart, lung and legs.
    Riding: 175 calories per half hour. Good for thigh and will training.
    Water skiing: 240 calories per half hour. It has a good exercise effect on the whole body, limbs muscles and balance ability.
    Golf: 125 calories per half hour. Its training effect comes from the long journey and batting action. If we can persevere, it is very beneficial to keep the lines beautiful.
    Jogging: 300 calories per half hour. Good for heart, lung and blood circulation. The longer you run, the more calories you burn.
    Walking: 75 calories per half hour. It can improve blood circulation, move joints and help to lose weight.')

def gym_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /gym is issued."""
    update.message.reply_text('Methods of reducing fat: strength training plus aerobic
    Many people come to the gym only to run, can you reduce fat? Answer: of course. But this body will not be good, there will be muscle loss in the process of fat reduction, and the maintenance of the body is the need for muscle.
    Aerobic exercise is recommended to be maintained for more than 30 minutes at low and medium intensity. It's not that fat is consumed after 30 minutes, but that the proportion of energy supplied by fat increases with time. What is medium low intensity? There is no fixed standard for this, but it is generally maintained at 55% - 70% of the maximum heart rate during exercise.
    Maximum heart rate formula = 220 - one year old')

def add(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /add is issued."""
    try: 
        global redis1
        logging.info(context.args[0])
        msg = context.args[0]   # /add keyword <-- this should store the keyword
        redis1.incr(msg)
        update.message.reply_text('You have said ' + msg +  ' for ' + redis1.get(msg).decode('UTF-8') + ' times.')
    except (IndexError, ValueError):
        update.message.reply_text('Usage: /add <keyword>')



if __name__ == '__main__':
    main()