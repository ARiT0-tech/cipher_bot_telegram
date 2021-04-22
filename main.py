from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler, CommandHandler, CallbackContext
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from lib import cip_keyboard, reply_keyboard, return_keyboard
from caesars import caesars_cipher
from enigma import enigma_code
from code import from_cipher, to_cipher
from morse import morse, demorse
from braille import debraille_code, braille_code
from db_handler import create_history, print_history, check, db_create
import os

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
com_return = ReplyKeyboardMarkup(return_keyboard, one_time_keyboard=False)
cip = ReplyKeyboardMarkup(cip_keyboard, one_time_keyboard=False)

TOKEN = '1751999231:AAEDSJALf8fgXIySv0wfDVYg6aE-LLJgYHg'


def start(update, context):
    context.user_data['id'] = check(update)
    update.message.reply_text(
        f"Выбирите тип шифра:", reply_markup=markup)
    return 1


def close_keyboard(update, context):
    update.message.reply_text('OK', reply_markup=ReplyKeyboardRemove())


def stop(update, context):
    return ConversationHandler.END


def first_response(update, context):
    text = update.message.text
    if text == 'Enigma':
        context.user_data['cipher'] = text
        update.message.reply_text(
            "Что делать будем?", reply_markup=cip)
    elif text == 'Шифр Цезаря':
        context.user_data['cipher'] = text
        update.message.reply_text(
            "Что делать будем?", reply_markup=cip)
    elif text == 'Braille':
        context.user_data['cipher'] = text
        update.message.reply_text(
            "Что делать будем?", reply_markup=cip)
    elif text == 'Двоичный код':
        context.user_data['cipher'] = text
        update.message.reply_text(
            "Что делать будем?", reply_markup=cip)
    elif text == 'Morse':
        context.user_data['cipher'] = text
        update.message.reply_text(
            "Что делать будем?", reply_markup=cip)
    elif text == 'return':
        close_keyboard(update, context)
        return ConversationHandler.END
    elif text == 'history':
        update.message.reply_text(print_history(context.user_data['id']))
        return 1
    else:
        update.message.reply_text(
            "Чего не умею, того не умею.")
    return 4


def second_response(update, context):
    text = update.message.text
    if text == 'return':
        update.message.reply_text('OK', reply_markup=markup)
        return 1
    elif text == 'history':
        update.message.reply_text(print_history(context.user_data['id']))
        return 4
    elif text.lower() == 'Зашифровать'.lower():
        if context.user_data['cipher'].lower() == 'Enigma'.lower():
            update.message.reply_text(
                "Для начала нужно ввести 3 ключя для роторов,\n"
                " а затем через '-' ввести текст на англиском,\n"
                " состояший только из букв и пробелов.\n"
                " Пример: ABC-Hello World.",
                reply_markup=com_return)
            return 5
        elif context.user_data['cipher'].lower() == 'Двоичный код'.lower():
            answer = """Ввод: <текст>"""
            update.message.reply_text(answer, reply_markup=com_return)
        elif context.user_data['cipher'].lower() == 'Шифр Цезаря'.lower():
            answer = "Ввод: <ключ>-<текст>\n" \
                     "Ключ-Одно число от 1 до 26."
            update.message.reply_text(answer, reply_markup=com_return)
        elif context.user_data['cipher'].lower() == 'Morse'.lower():
            answer = "Ввод: <текст>\n" \
                     "Текст только на английском"
            update.message.reply_text(answer, reply_markup=com_return)
        elif context.user_data['cipher'].lower() == 'Braille'.lower():
            answer = "Ввод: <текст>\n" \
                     "Текст только на английском, без цифр"
            update.message.reply_text(answer, reply_markup=com_return)
        return 2
    elif text.lower() == 'Расшифровать'.lower():
        if context.user_data['cipher'].lower() == 'Enigma'.lower():
            update.message.reply_text(
                "Для начала нужно ввести 3 ключи для роторов,\n"
                "которые были использованный для шифровки,"
                "затем через '-' ввести шифр только на англиском,\n"
                "состояший только из букв и пробелов.\n"
                "Пример: ABC-FPXKE HWZEQ.",
                reply_markup=com_return)
            return 5
        elif context.user_data['cipher'].lower() == 'Двоичный код'.lower():
            answer = """Ввод: <код>"""
            update.message.reply_text(answer, reply_markup=com_return)
        elif context.user_data['cipher'].lower() == 'Шифр Цезаря'.lower():
            answer = "Ввод: <ключ>-<шифр>\n" \
                     "Ключ-Число, которое использовалось для шифровки."
            update.message.reply_text(answer, reply_markup=com_return)
        elif context.user_data['cipher'].lower() == 'Morse'.lower():
            answer = """Ввод: <шифр>"""
            update.message.reply_text(answer, reply_markup=com_return)
        elif context.user_data['cipher'].lower() == 'Braille'.lower():
            answer = "Ввод: <шифр>"
            update.message.reply_text(answer, reply_markup=com_return)
        return 3
    return 4


def enigma_response(update, context):
    text = update.message.text
    if text == 'return':
        update.message.reply_text('OK', reply_markup=cip)
        return 4
    elif text == 'history':
        update.message.reply_text(print_history(context.user_data['id']))
        return 5
    else:
        try:
            enigma = enigma_code(text)
            create_history(context.user_data['id'], text, f"{''.join(enigma)}")
        except Exception:
            update.message.reply_text('Вы вели слишком много ключей\n'
                                      'или ошиблись в типе данных, ввели посторонние символы!')
            return 5
        update.message.reply_text(f"{''.join(enigma)}")
    return 5


def encrypt_response(update, context):
    text = update.message.text
    db_text = text
    if text == 'return':
        update.message.reply_text('OK', reply_markup=cip)
        return 4
    elif text == 'history':
        update.message.reply_text(print_history(context.user_data['id']))
        return 2
    if context.user_data['cipher'].lower() == 'Двоичный код'.lower():
        cipher_text = to_cipher(text)
    elif context.user_data['cipher'].lower() == 'Morse'.lower():
        try:
            cipher_text = morse(text)
        except Exception:
            update.message.reply_text('Ошибка в типе введенных данных.')
    elif context.user_data['cipher'].lower() == 'Braille'.lower():
        try:
            cipher_text = braille_code(text)
            if len(cipher_text) == 0:
                update.message.reply_text('Ошибка в типе введенных данных.')
                return 2
        except Exception:
            update.message.reply_text('Ошибка в типе введенных данных.')
    elif context.user_data['cipher'].lower() == 'Шифр Цезаря'.lower():
        try:
            key, text = text.split('-')[0], text.split('-')[1]
            if int(key) > 26 or int(key) < 1:
                update.message.reply_text('Неправильный ключ')
                return 2
            cipher_text = caesars_cipher(int(key), text)
            if len(cipher_text) == 0:
                update.message.reply_text('Ошибка в типе введенных данных.')
                return 2
        except Exception:
            update.message.reply_text('Вы вели слишком много ключей\n'
                                      'или ошиблись в типе данных, ввели посторонние символы!')
    create_history(context.user_data['id'], db_text, f"{cipher_text}")
    update.message.reply_text(
        f"{cipher_text}")
    return 2


def decrypt_response(update, context):
    text = update.message.text
    db_text = text
    if text == 'return':
        update.message.reply_text('OK', reply_markup=cip)
        return 4
    elif text == 'history':
        update.message.reply_text(print_history(context.user_data['id']))
        return 3
    if context.user_data['cipher'].lower() == 'Двоичный код'.lower():
        try:
            cipher_text = from_cipher(text)
        except Exception:
            update.message.reply_text('Вы точно ввели код')
    elif context.user_data['cipher'].lower() == 'Morse'.lower():
        try:
            cipher_text = demorse(text)
            if len(cipher_text) == 0:
                update.message.reply_text('Ошибка в типе введенных данных.')
                return 3
            elif cipher_text is None:
                update.message.reply_text('Ошибка в типе введенных данных.')
                return 3
        except Exception:
            update.message.reply_text('Ошибка в типе введенных данных.')
    elif context.user_data['cipher'].lower() == 'Braille'.lower():
        try:
            cipher_text = debraille_code(text)
            if len(cipher_text) == 0:
                update.message.reply_text('Ошибка в типе введенных данных.')
                return 3
            elif cipher_text is None:
                update.message.reply_text('Ошибка в типе введенных данных.')
                return 3
        except Exception:
            update.message.reply_text('Ошибка в типе введенных данных.')
    elif context.user_data['cipher'].lower() == 'Шифр Цезаря'.lower():
        try:
            key, text = text.split('-')[0], text.split('-')[1]
            if int(key) > 26 or int(key) < 1:
                update.message.reply_text('Неправильный ключ')
                return 3
            cipher_text = caesars_cipher(int(key) * -1, text)
            if len(cipher_text) == 0:
                update.message.reply_text('Ошибка в типе введенных данных.')
                return 3
        except Exception:
            update.message.reply_text('Вы вели слишком много ключей\n'
                                      'или ошиблись в типе данных, ввели посторонние символы!')
    create_history(context.user_data['id'], db_text, f"{cipher_text}")
    update.message.reply_text(
        f"{cipher_text}")
    return 3


def remove_job_if_exists(name, context):
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True


cipher = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        1: [MessageHandler(Filters.text, first_response)],
        2: [MessageHandler(Filters.text, encrypt_response)],
        3: [MessageHandler(Filters.text, decrypt_response)],
        4: [MessageHandler(Filters.text, second_response)],
        5: [MessageHandler(Filters.text, enigma_response)],
    },
    fallbacks=[CommandHandler('stop', stop)])

if __name__ == '__main__':
    db_create()
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(cipher)
    port = int(os.environ.get("PORT", 5000))
    updater.start_webhook(listen='0.0.0.0', port=port, url_path=TOKEN,
                          webhook_url="https://app-telebot228.herokuapp.com/" + TOKEN)
    updater.idle()
