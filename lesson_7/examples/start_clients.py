from subprocess import Popen

clients_processes_list = []
while True:
    user = input(
        "Запустить 10 клиентов (s) / Закрыть клиентов (x) / Выйти (q) "
    )
    if user == 'q':
        break
    elif user == 's':
        for _ in range(10):
            # Флаг CREATE_NEW_CONSOLE нужен для ОС Windows,
            # чтобы каждый процесс запускался в отдельном окне консоли
            clients_processes_list.append(
                Popen(
                    'python time_client_random.py',
                    # creationflags=CREATE_NEW_CONSOLE
                )
            )
            print(' Запущено 10 клиентов')
    elif user == 'x':
        for p in clients_processes_list:
            p.kill()

        clients_processes_list.clear()
