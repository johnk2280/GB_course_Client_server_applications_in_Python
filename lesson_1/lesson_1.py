import chardet

from controllers import (
    get_type,
    get_bytes,
    there_and_back,
    get_ping_result,
)

from const import (
    WORDS,
    WORDS_UTF,
    URLS,
)

print('-------------------------------task 1---------------------------------------')
"""
1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
и также проверить тип и содержимое переменных.

"""

for word in WORDS:
    print(get_type(word))

print()

for word in WORDS_UTF:
    print(get_type(word))

print('-------------------------------task 2-3--------------------------------------')
"""
2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность 
кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

"""

for word in WORDS:
    print(get_bytes(word), '', sep='\n')

print('-------------------------------task 4----------------------------------------')
""" 
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое 
и выполнить обратное преобразование (используя методы encode и decode).

"""

for word in WORDS:
    print(there_and_back(word), '', sep='\n')

print('-------------------------------task 5----------------------------------------')
"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и 
преобразовать результаты из байтового в строковый тип на кириллице.

"""

for url in URLS:
    print(get_ping_result(url), '', sep='\n')

print('-------------------------------task 6----------------------------------------')
"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: 
«сетевое программирование», «сокет», «декоратор». 
Проверить кодировку файла по умолчанию. 
Принудительно открыть файл в формате Unicode и вывести его содержимое.

"""

with open('test_file.txt', 'wb') as f:
    f.writelines(word.encode() + b'\n' for word in WORDS)

with open('test_file.txt', 'rb') as f_obj:
    content = f_obj.read()
    encoding = chardet.detect(content)['encoding']
    print(encoding)


with open('test_file.txt', 'r', encoding=encoding) as f:
    result = f.readlines()

print(*result)
