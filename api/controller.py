import logging
import telegram_api

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')

def sendasync_controller(data):
    if 'USER' in data and 'MSG' in data:
        try:
            return telegram_api.send_message(data['USER'], data['MSG'])
        except Exception as e:
            logging.error(e)
            return {'error': 'error while sending msg : controller'}
    else:
        return {'error': 'USER and MSG params should be present in the POST body'}