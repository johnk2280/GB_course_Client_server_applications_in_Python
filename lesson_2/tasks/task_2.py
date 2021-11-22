"""
2. Задание на закрепление знаний по модулю json.
Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными.

Для этого:
    - Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
      цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде
      словаря в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;

    - Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.

"""
import datetime
import json

from settings import (
    TEST_FILE_DIR,
    ORDERS,
    get_files,
)


def write_order_to_json(orders: list) -> None:
    files = get_files(TEST_FILE_DIR, 'json')
    for file in files:
        with open(TEST_FILE_DIR.joinpath(file), 'r') as f_obj:
            content = f_obj.read()
            obj = json.loads(content)
            obj['orders'].extend(orders)
            print(1)

        with open(TEST_FILE_DIR.joinpath(file), 'w', encoding='utf-8') as f_obj:
            json.dump(obj, f_obj, sort_keys=True, indent=4)


if __name__ == '__main__':
    write_order_to_json(ORDERS)
