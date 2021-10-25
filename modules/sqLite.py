import sqlite3


# Пользователь проверяет себя по базе данных
def read_value_table_name(
        graph: str,
        table: str,
        telegram_id: int, *,
        id_name: str = 'telegram_id'):
    connect = sqlite3.connect('modules/database.db')
    curs = connect.cursor()
    for data in curs.execute(f'SELECT {graph} FROM {table} WHERE {id_name} ="{telegram_id}"'):
        return data
    connect.close()


# Пользователь проверяет себя по базе данных
def read_all(
        name: str,
        table: str):
    connect = sqlite3.connect('modules/database.db')
    curs = connect.cursor()
    curs.execute(f'SELECT {name} FROM {table}')
    data = curs.fetchall()
    return data


# Создаем первую запись в бд
def insert_first_note(
        table: str,
        telegram_id: int, *,
        id_name: str = 'telegram_id'):
    connect = sqlite3.connect('modules/database.db')
    curs = connect.cursor()
    curs.execute(f"INSERT INTO {table} ({id_name}) VALUES ('{telegram_id}')")
    connect.commit()
    connect.close()


# Обновляем любые данные в любую таблицу
def insert_info(
        table: str,
        telegram_id: int,
        name: str,
        data, *,
        id_name: str = 'telegram_id'):
    connect = sqlite3.connect('modules/database.db')
    curs = connect.cursor()
    curs.execute(f"UPDATE {table} SET {name}= ('{data}') WHERE {id_name}='{telegram_id}'")
    connect.commit()
    connect.close()


# Читаем данные в таблице
def read_values_by_name(table: str, 
                        data, *,
                        id_name: str = 'telegram_id',
                        name: str = '*'):
    connect = sqlite3.connect('modules/database.db')
    curs = connect.cursor()
    for d in curs.execute(f'SELECT {name} FROM {table} WHERE "{id_name}" = "{data}"'):
        return d
    connect.close()


# Удаляем данные из таблицы
def delete_str(
        table: str,
        data, *,
        name: str = 'telegram_id'):
    connect = sqlite3.connect('modules/database.db')
    curs = connect.cursor()
    curs.execute(f"DELETE FROM '{table}' WHERE {name}={data}")
    connect.commit()
    connect.close()
