from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from config import API_TOKEN

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)

# Инициализируем объект dp
dp = Dispatcher(bot=bot)


def start(bot, update):
    update.message.reply_text('Привет! Я информационный бот компании "Путешествия и туризм".\n'
                              'Для получения информации можете воспользоваться подсказками ниже!',
                              reply_markup=markup) 

def task(bot, job):
    bot.send_message(job.context, text='Хорош сидеть за компьютером, разомнись!')

def set_timer(bot, update, job_queue, chat_data):
    
    # создаём задачу task в очереди job_queue
    # передаём ей идентификатор текущего чата
    # идентификатор далее будет доступен через job.context
    
    delay = 5 # количество секунд
    job = job_queue.run_once(task, delay, context=update.message.chat_id)

    # Регистрируем созданную задачу в пользовательских данных
    chat_data['job'] = job
    
    # Сообщаем о том, что таймер установлен
    update.message.reply_text('Таймер установлен на ' + delay + ' секунд' )
    
def unset_timer(bot, update, chat_data):
    # Проверяем, что задача ставилась (вот зачем нужно было ее записать в chat_data).
    if 'job' in chat_data:
        # планируем удаление задачи
        chat_data['job'].schedule_removal()
        # и очищаем пользовательские данные
        del chat_data['job']

    update.message.reply_text('Таймер отменён!')
    
def echo(bot, update):
    if update.message.text[-1] == '?':
        update.message.reply_text('Конечно можно спросить! Только я культурно промолчу...')
    else:
        update.message.reply_text('Вполне возможно, кто ж знает?')
    

updater = Updater('1214407282:AAE2HtWxWu1cwpB7sbYqZg913FnldHjOtfc')

dp = updater.dispatcher

reply_keyboard = [['/set_timer', '/unset_timer']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

dp.add_handler(CommandHandler('start', start))
dp.add_handler(CommandHandler('close', close_keyboard))

dp.add_handler(CommandHandler("set_timer", set_timer, pass_job_queue=True, pass_chat_data=True))
dp.add_handler(CommandHandler("unset_timer", unset_timer, pass_chat_data=True))

text_handler = MessageHandler(Filters.text, echo)
dp.add_handler(text_handler)

updater.start_polling()

updater.idle()