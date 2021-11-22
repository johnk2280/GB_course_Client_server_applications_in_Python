import os
import re
from datetime import datetime

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TEST_FILE_DIR = BASE_DIR.joinpath('test_files')

ORDER = {
    'item': 'apple',
    'quantity': 225,
    'price': 0.4,
    'buyer': 'JohnK',
    'date': datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),

}
ORDERS = [ORDER, ]

DATA_TO_YAML = {
    '1€': [1, 2, 'spam', 'egg', 7, 'foo'],
    '2€': 2,
    '3€': ORDER
}


def get_files(directory, file_extension=None):
    all_files = os.listdir(directory)
    for file in all_files:
        if re.search(file_extension, file):
            yield file
