"""
1. Задание на закрепление знаний по модулю CSV.
Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий
новый «отчетный» файл в формате CSV.

Для этого:
    - Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными,
      их открытие и считывание данных. В этой функции из считанных данных необходимо с помощью регулярных выражений
      извлечь значения параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
      Значения каждого параметра поместить в соответствующий список. Должно получиться четыре списка — например,
      os_prod_list, os_name_list, os_code_list, os_type_list.
      В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить в него
      названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
      Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);

    - Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
      В этой функции реализовать получение данных через вызов функции get_data(),
      а также сохранение подготовленных данных в соответствующий CSV-файл;

    - Проверить работу программы через вызов функции write_to_csv().

"""

import os
import re
import csv

from pathlib import Path
import chardet

BASE_DIR = Path(__file__).resolve().parent.parent
TEST_FILE_DIR = BASE_DIR.joinpath('test_files')


def get_files(directory, file_extension=None):
    all_files = os.listdir(directory)
    for file in all_files:
        if re.search(file_extension, file):
            yield file


def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [
        'Изготовитель системы',
        'Название ОС',
        'Код продукта',
        'Тип системы'
    ]
    for file in get_files(TEST_FILE_DIR, '.txt'):
        with open(TEST_FILE_DIR.joinpath(file), 'rb') as f_obj:
            content = f_obj.read()
            encoding_params = chardet.detect(content)
            lines = content.decode(encoding_params['encoding']).split('\r\n')
            for line in lines:

                print(line)

        print('------------------------------------------------------------------------')


def write_to_csv():
    pass


if __name__ == '__main__':
    get_data()
