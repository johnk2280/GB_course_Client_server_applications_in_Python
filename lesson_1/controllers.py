import subprocess

import chardet


def get_type(word):
    return f'{word} - {type(word)}'


def get_bytes(word):
    try:
        word = eval(f'b"{word}"')
        return f'{type(word)}\n{word}\n{len(word)}'
    except SyntaxError:
        return f'слово "{word}" невозможно преобразовать в байты без указания кодировки'


def there_and_back(word: str):
    w = word.encode('utf8')
    return f'{w}\n{w.decode("utf-8")}'


def get_ping_result(url):
    result = ''
    subproc_ping = subprocess.Popen(
        ['ping', '-c', '4', url],
        stdout=subprocess.PIPE,
    )
    for line in subproc_ping.stdout:
        data = chardet.detect(line)
        line = line.decode(data["encoding"])
        result += f'{line}'

    return result
