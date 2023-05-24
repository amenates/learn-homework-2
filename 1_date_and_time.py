"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

from datetime import datetime, timedelta


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    dt_now = datetime.now()
    delta = timedelta(days=30)
    print(f"Сегодняшняя дата: {dt_now.strftime('%d.%m.%Y %H:%m')}")
    print(
        f"30 дней назад была дата: {(dt_now - delta).strftime('%d.%m.%Y %H:%m')}"
    )


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    return datetime.strptime(date_string, "%m/%d/%y %H:%M:%S.%f")


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
