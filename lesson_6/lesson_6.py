"""
1. Продолжая задачу логирования, реализовать декоратор @log,
    фиксирующий обращение к декорируемой функции.
    Он сохраняет ее имя и аргументы.

2. В декораторе @log реализовать фиксацию функции,
    из которой была вызвана декорированная. Если имеется такой код:
@log
def func_z():
 pass

def main():
 func_z()
...в логе должна быть отражена информация:
"<дата-время> Функция func_z() вызвана из функции main"
"""
