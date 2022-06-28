import logging
import logging.handlers
import sys

from settings import BASE_DIR
from settings import LOGGER_CONFIG

sys.path.append('../')
PATH_TO_LOG = BASE_DIR.joinpath('logs', 'client.log')

# init formatter
normal_format = LOGGER_CONFIG['formatters']['normal']['format']
client_formatter = logging.Formatter(normal_format)

# init output streams
client_handler = logging.StreamHandler(sys.stdout)
client_handler.setFormatter(client_formatter)
client_handler.setLevel(logging.DEBUG)
log_file = logging.handlers.RotatingFileHandler(
    PATH_TO_LOG,
    encoding='utf8',
    maxBytes=1048576,
    backupCount=6,
)
log_file.setFormatter(client_formatter)
log_file.setLevel(logging.DEBUG)

client_logger = logging.getLogger('client')
client_logger.addHandler(client_handler)
client_logger.addHandler(log_file)
client_logger.setLevel(logging.DEBUG)


if __name__ == '__main__':
    client_logger.critical('Критическая ошибка')
    client_logger.error('Ошибка')
    client_logger.debug('Отладочная информация')
    client_logger.info('Информационное сообщение')