import logging
import logging.handlers
import sys

from settings import BASE_DIR
from settings import LOGGER_CONFIG

sys.path.append('../')
PATH_TO_LOG = BASE_DIR.joinpath('logs', 'server.log')

# init formatter
normal_format = LOGGER_CONFIG['formatters']['normal']['format']
server_formatter = logging.Formatter(normal_format)

# init output streams
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(server_formatter)
stream_handler.setLevel(logging.DEBUG)
log_file = logging.handlers.RotatingFileHandler(
    PATH_TO_LOG,
    encoding='utf8',
    maxBytes=1048576,
    backupCount=6,
)
log_file.setFormatter(server_formatter)
log_file.setLevel(logging.DEBUG)


server_logger = logging.getLogger('server')
server_logger.addHandler(stream_handler)
server_logger.addHandler(log_file)
server_logger.setLevel(logging.DEBUG)


if __name__ == '__main__':
    server_logger.critical('Критическая ошибка')
    server_logger.error('Ошибка')
    server_logger.debug('Отладочная информация')
    server_logger.info('Информационное сообщение')