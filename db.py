import sqlite3
from typing import Any, Callable

db_path = 'db.db'

def db_connect(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        with sqlite3.connect(database=db_path) as conn:
            cursor = conn.cursor()
            result = func(*args,cursor=cursor, **kwargs)
            conn.commit()
        
        return result
        
    return wrapper

def __create_users_db(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE users (
        name text,
        password text)''')

def __create_tasks_db(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE tasks (
        title text,
        text text,
        timestamp int,
        status text,
        user_id int)''')

@db_connect
def __setting_tables(cursor):
    __create_users_db(cursor=cursor)
    __create_tasks_db(cursor=cursor)
    
if __name__ == '__main__':
    __setting_tables()
