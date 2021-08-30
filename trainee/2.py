import time
import datetime
from typing import Any, Callable


def logging_func(func: Callable) -> Any:
    """
    Декоратор логирования обернутой функции
    """
    def wrapped_func(*args, **kwargs):
        start_timer = time.time()
        try:
            result = func(*args, **kwargs)
            stop_timer = time.time()
            result_timer = round(stop_timer - start_timer, 3)
            print(f'функция выполнилась успешно!\nПотраченое время: {result_timer}')
            return result
        except Exception as exc:
            cur_time = datetime.datetime.now().strftime('%d/%m/%y %H:%M:%S')
            print('Была допущена ощибка! Логи ошибки записаны в log.txt')
            logg_file = open('log.txt', 'a', encoding='utf-8')  # лог файл добавляется, а не перезаписывается
            error = f'[{str(cur_time)}]:  Функция: "{func.__name__}" - получила ошибку с кодом: {exc} \n '
            logg_file.write(error)
            logg_file.close()
            raise
    return wrapped_func


@logging_func
def broken_func() -> Any:
    """
    функция которая может быть поломана
    """
    all_names = list()
    try:
        file = open('names.txt', 'r', encoding='utf-8')
    except FileNotFoundError('Не найден файл!'):
        raise FileNotFoundError('Отсутствует файл "names.txt" в корневом каталоге!')
    for name in file:
        name = name.rstrip()
        if len(name) < 3:  # Проверка на длинну имени
            raise TypeError('В этой программе имя не может быть короче 3 букв!')
        if not name.replace(' ', '').isalpha():
            # Проверка имени на символы без учета пробела, ибо может быть введено ФИО
            raise TypeError('В имени не должно содержатся цифр и символов!')
        else:
            all_names.append(name)

    file.close()
    return all_names


print(broken_func())
