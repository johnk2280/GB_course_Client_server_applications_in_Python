import logging
import logging.handlers
import sys

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PATH = BASE_DIR.joinpath('log', 'client.log')

client_formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(filename)s %(message)s')

client_handler = logging.StreamHandler(sys.stderr)
client_handler.setFormatter(client_formatter)
client_handler.setLevel(logging.ERROR)
log_file = logging.handlers.TimedRotatingFileHandler(PATH, encoding='utf8', interval=1, when='S')
log_file.setFormatter(client_formatter)


client_logger = logging.getLogger('client')
client_logger.addHandler(client_handler)
client_logger.addHandler(log_file)
client_logger.setLevel(logging.DEBUG)


if __name__ == '__main__':
    client_logger.critical('Критическая ошибка')
    client_logger.error('Ошибка')
    client_logger.debug('Отладочная информация')
    client_logger.info('Информационное сообщение')