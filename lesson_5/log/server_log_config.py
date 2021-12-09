import logging
import logging.handlers
import sys

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PATH = BASE_DIR.joinpath('log', 'server.log')

server_formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(filename)s %(message)s')

stream_handler = logging.StreamHandler(sys.stderr)
stream_handler.setFormatter(server_formatter)
stream_handler.setLevel(logging.ERROR)
log_file = logging.handlers.TimedRotatingFileHandler(PATH, encoding='utf8', interval=1, when='S')
log_file.setFormatter(server_formatter)


server_logger = logging.getLogger('server')
server_logger.addHandler(stream_handler)
server_logger.addHandler(log_file)
server_logger.setLevel(logging.DEBUG)


if __name__ == '__main__':
    server_logger.critical('Критическая ошибка')
    server_logger.error('Ошибка')
    server_logger.debug('Отладочная информация')
    server_logger.info('Информационное сообщение')