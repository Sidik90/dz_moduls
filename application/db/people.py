from application.datetime import current_moscow_time


def get_employees():
    print(current_moscow_time.strftime('%Y-%m-%d %H:%M:%S'))
    print('Работает get_employees')