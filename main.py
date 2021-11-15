import sqlite3
import os

file_name = os.path.abspath(os.path.join('data_base', 'temp.db'))


def sql_connection() -> sqlite3.Connection:
    """ Функция для подключения к базу данных """
    try:
        with sqlite3.connect(file_name) as clients:
            print('Подключение к базе успешно')
        return clients

    except Exception as err:
        print('Ошибка при подключении к базе:\n{err}'.format(err=err))


def sql_table(clients) -> None:
    """ Функция создает имя таблицы если она не существует """

    cursor = clients.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS reestr ("
                   "user_id INTEGER,"
                   "name TEXT,"
                   "age INTEGER"
                   ")")
    clients.commit()
    print('Данные добавлены')


client = sql_connection()
sql_table(clients=client)

# TODO продолжение следует ...
