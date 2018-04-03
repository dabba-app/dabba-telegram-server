import logging
import telegram_bot
import mongo_obj

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')

def send_message(user_name, message):
    try:
        client = mongo_obj.fetch_singleton()
        telegram = client.telegram_db.posts
        chat_id = telegram.find_one({"USER_NAME": str(user_name)})['C_ID']
        async_bot = telegram_bot.fetch_singleton()
        print(chat_id)
        print(message)
        async_bot.send_message(chat_id, message)
        return {'success': 'msg sent successfully'}
    except Exception as e:
        logging.error(e)
        error = 'error in telegram send_message fn' + e
        return {'error': error}