import os
import re

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TEST_FILE_DIR = BASE_DIR.joinpath('test_files')


def get_files(directory, file_extension=None):
    all_files = os.listdir(directory)
    for file in all_files:
        if re.search(file_extension, file):
            yield file
