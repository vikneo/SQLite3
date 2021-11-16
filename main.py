import sqlite3
import os

file_name = os.path.abspath(os.path.join('data_base', 'temp.db'))


def sql_connection(path: str) -> sqlite3.Connection:
    """ Функция для подключения к базу данных """
    try:
        with sqlite3.connect(path) as clients:
            print('Подключение к базе успешно')
        return clients

    except Exception as err:
        print('Ошибка при подключении к базе:\n{err}'.format(err=err))


def sql_table(clients: sqlite3.Connection, name_db: str) -> None:
    """ Функция создает имя таблицы если она не существует """

    cursor = clients.cursor()
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {name_db} ("
                   "user_id INTEGER PRIMARY KEY,"
                   "first_name TEXT,"
                   "second_name TEXT,"
                   "gender TEXT"
                   ")")
    clients.commit()
    print('Таблица создана')


def select_base(clients: sqlite3.Connection, command: str, name: str, limit: int = None) -> list:
    """ Функция для выборки данных из БД 
    

    :param clients: (sqlite3.Connection) - подключение к базе данных
    :param command: (str): - ввод команды для выборки из базы
    :param name: (str): - имя таблицы в базе
    :param limit: (int): - параметр LIMIT для вывода данных

    """

    cursor = clients.cursor()

    cursor.execute(f"""SELECT {command} FROM {name} {[f' LIMIT {limit}' if limit is not None else ''][0]}""")
    result = cursor.fetchall()
    clients.commit()
    print('Данные считаны')
    return result


def insert_base(clients: sqlite3.Connection, data: list, name_db: str) -> None:
    """ Функция для внесения данных в БД """

    cursor = clients.cursor()
    for row in data:
        cursor.execute(f"INSERT INTO {name_db} VALUES(?, ?, ?, ?);", row)
        clients.commit()
    print('Данные добавлены')


if __name__ == '__main__':
    client = sql_connection(file_name)
    if client:
        # sql_table(clients=client, name_db='users')
        # sql_table(clients=client, name_db='orders')
        # insert_base(clients=client, data=customers, name_db='users')
        # insert_base(clients=client, data=orders, name_db='orders')

        data_base = select_base(clients=client,
                                command='user_id, first_name, second_name',
                                name='users',
                                #limit=3
                                )

        print('Считываем с базы:')
        for elem in data_base:
            print(*elem)
        print()
