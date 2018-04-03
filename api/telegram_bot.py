async_bot = None

def fetch_singleton():
    global async_bot
    if async_bot is None:
        import os
        import telebot
        token = os.environ.get('TELEGRAM_KEY')
        async_bot = telebot.AsyncTeleBot(token)
    return async_bot
