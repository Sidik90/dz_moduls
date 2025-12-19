from application.datetime import current_moscow_time


def calculate_salary():
    print(current_moscow_time.strftime('%Y-%m-%d %H:%M:%S'))
    print('Работает calculate_salary')