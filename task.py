from user import User
from datetime import datetime

class Task:
    def __init__(self, title, text, timestamp=int(datetime.now().timestamp()), status='Created') -> None:
        self.title = title
        self.text = text
        self.timestamp = timestamp 
        self.status = status 

    def __str__(self) -> str:
        return f'Title: {self.title}\nText: {self.text}\nCreate date: { datetime.fromtimestamp(self.timestamp).strftime("%d.%m.%y")}'  


class TaskManager:
 
    def __init__(self, user:User) -> None:
        self.user:User = user

    def create_task(self):
        title = input('Write task title\n')
        text = input('Write task text\n')

        task = Task(title=title, text=text)
        self.save_user_task(task=task)


    def view_tasks(self):
        tasks = self.load_user_tasks()
        if tasks == []:
            print('No tasks')
        else:
            print(f'You have {len(tasks)} tasks:',
                  *[f'{i+1}:{task.title}' for i, task in enumerate(tasks)],
                  sep='\n')
        return len(tasks)

    def check_task(self):
        task_amount = self.view_tasks()
        if task_amount != 0:
            while True:
                task_id = input('Enter id of the task you want to view, or 0 if you want to return to the menu:\n')
                
                if task_id == '0':
                    break
                else: 
                    print(self.load_user_tasks()[int(task_id)-1]) 


    def change_task_status(self, task:Task):
        status = input('Enter status:\n')
        task.status = status
    
    def load_user_tasks(self) -> list[Task]:
        tasks = list()
        lines = list()
        with open(self.user.tasks_path, 'r') as f:
            lines = f.readlines()
        
        if lines:
            for line in lines:
                title, text, timestamp, status = [x.split(':')[-1] for x in line.strip().split(',')] 
                task = Task(title=title, text=text, timestamp=int(timestamp), status=status) 
                
                tasks.append(task)

        return tasks

    def save_user_task(self, task:Task):
        task_dict = task.__dict__
        with open(self.user.tasks_path, 'a+') as f:
            f.write(','.join([f'{key}:{task_dict[key]}' for key in task_dict]) + '\n')



