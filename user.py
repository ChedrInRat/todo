from db import db_connect
from sqlite3 import Cursor


class User:

    def __init__(self, name:str, id:int|None) -> None:
        self.__id:None|int = id
        self._name = name 
        self._login = False

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self.update()

    def __str__(self) -> str:
        return f'Name: {self._name}'
    
    @db_connect
    def login(self, cursor:Cursor, password:str) -> bool:
        cursor.execute(f"SELECT password FROM users WHERE rowid={self.__id}") 
        pwd = cursor.fetchone()   
        self._login = True if pwd[0] == password else False  

        return self._login 

    @db_connect
    def update(self, cursor:Cursor):
        cursor.execute(f"UPDATE users SET name='{self._name}' WHERE rowid={self.__id}'")

    def unlogin(self):
        self._login = False
    

class UserHandler:
    
    @staticmethod
    @db_connect
    def create(cursor:Cursor, name:str, password:str) -> User:
        cursor.execute(f"INSERT INTO users (name, password) VALUES ('{name}', '{password}')")
        return User(name=name, id=cursor.lastrowid)


    @staticmethod
    @db_connect
    def get_by_name(cursor:Cursor, name:str) -> User:
        cursor.execute(f"SELECT name, rowid FROM users WHERE name='{name}'") 
        user = cursor.fetchone()
        return User(name=user[0], id=user[1])

    @staticmethod
    @db_connect
    def get_by_id(cursor:Cursor, user_id:int) -> User:
        cursor.execute(f"SELECT name, rowid FROM users WHERE rowid={user_id}") 
        user = cursor.fetchone()
        return User(name=user[0], id=user[1])

    @staticmethod
    @db_connect
    def delete(cursor:Cursor, id:int):
        cursor.execute(f"DELETE FROM users WHERE rowid={id}") 

    
    @staticmethod
    @db_connect
    def get_list(cursor:Cursor) -> tuple[User,...]|None:
        cursor.execute("SELECT name, rowid FROM users")
        users = cursor.fetchall()
        answer = tuple(User(name=name, id=rowid) for name, rowid in users) if users else None
        return answer 
    

class UserManager():
    
    @staticmethod
    def create_user():
        name = input('Write you name: ')
        pwd = input('Write password: ')

        UserHandler.create(name=name, password=pwd) 
    
    @staticmethod
    def login_user(user:User) -> bool:
        pwd = input('Write password: ') 
        
        return user.login(password=pwd) 
        

    

