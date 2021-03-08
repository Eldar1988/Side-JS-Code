import telebot


bot = telebot.TeleBot('1638154879:AAHa9jt6N2GX5_sg7Lc9wb8yQUQd51yecSM')
chat_id = '1632019718'


def tg_send_call_back(callback):
    """Заявка"""
    name = callback.name
    phone = callback.phone
    comment = callback.text
    service = callback.service
    text = f'=====   Заявка ===== \n\n' \
           f'Имя: {name} \n' \
           f'Телефон: {phone} \n' \
           f'Комментарий: {comment} \n' \
           f'Услуга: {service} \n' \

    bot.send_message(chat_id, text)
