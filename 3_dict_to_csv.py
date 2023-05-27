"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору.
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

import csv


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    persons = [{
        'name': 'Julia',
        'age': '34',
        'job': 'Engineer'
    }, {
        'name': 'Anna',
        'age': '21',
        'job': 'Salesman'
    }, {
        'name': 'Mike',
        'age': '50',
        'job': 'Driver'
    }, {
        'name': 'David',
        'age': '26',
        'job': 'Firefighter'
    }]

    with open('export.csv', 'w', encoding='utf-8') as export:
        fielsd = ['name', 'age', 'job']
        writer = csv.DictWriter(export, fielsd, delimiter=';')
        writer.writeheader()
        for item in persons:
            writer.writerow(item)


if __name__ == "__main__":
    main()
