from user import User
from db import db_connect
from sqlite3 import Cursor
from datetime import datetime, time

class Task:
    def __init__(self, id:int|None, title:str, text:str, user_id:int, status:str,
                 timestamp=int(datetime.now().timestamp())) -> None:

        self.__id = id
        self._title = title
        self._text = text
        self._timestamp = timestamp 
        self._status = status 
        self._user_id = user_id 

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
        self.update()

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        self.update

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
        self.update  

    @db_connect
    def update(self, cursor:Cursor):
        cursor.execute(f"UPDATE tasks SET title='{self.title}' text='{self.text}' status='{self.status}' WHERE rowid={self.__id}") 


class TaskHandler:
    
    @staticmethod
    @db_connect
    def create_task(cursor:Cursor, title:str, text:str, user_id:int, status:str='Created') -> Task:
        timestamp = int(datetime.now().timestamp())
        cursor.execute(f"""INSERT INTO tasks (title, text, timestamp, status, user_id) VALUES ('{title}', '{text}', {timestamp}, '{status}', {user_id})""")
         
        return Task(id=cursor.lastrowid, title=title, text=text, status=status, user_id=user_id)
        

    @staticmethod
    @db_connect
    def get_task_by_id(cursor:Cursor, task_id) -> Task|None:
        cursor.execute(f"SELECT rowid, title, text, timestamp, status, user_id FROM tasks WHETE rowid={task_id}")
        task = cursor.fetchone()

        return Task(id=task[0], title=task[1], text=task[2], timestamp=task[3], status=task[4], user_id=task[5])

    @staticmethod
    @db_connect
    def delete_task(cursor:Cursor, task_id):
        cursor.execute(f"DELETE FROM tasks WHERE rowid={task_id}") 

    @staticmethod
    @db_connect
    def get_list(cursor:Cursor, user_id:int) -> tuple[Task,...]|None:
        cursor.execute(f"SELECT rowid, title, text, timestamp, status FROM tasks WHERE user_id={user_id}") 
        tasks = cursor.fetchall()
        answer = tuple(Task(id=rowid, title=title, text=text, timestamp=timestamp, status=status, user_id=user_id) 
                       for rowid, title, text, timestamp, status in tasks) if tasks else None

        return answer

    
    
class TaskManager:
    
    def __init__(self, user:User) -> None:
        self.user = user

    def create_task(self):
        title = input('Write task title: ')
        text = input('Write task text: ')

        TaskHandler.create_task(title=title, text=text, user_id=self.user.id)  
        

    def view_tasks(self):
        tasks = TaskHandler.get_list(user_id=self.user.id)
        if tasks == []:
            print('No tasks')
        else:
            print(f'You have {len(tasks)} tasks:',
                  *[f'{i+1}:{task.title}' for i, task in enumerate(tasks)],
                  sep='\n')
        return len(tasks)

       
