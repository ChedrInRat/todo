from datetime import datetime

class Task:
    def __init__(self, title, text) -> None:
        self.title = title
        self.text = text
        self.create_date = datetime.now()
        self.status: str = 'Created' 

    def __str__(self) -> str:
        return f'Title: {self.title}\nText: {self.text}\nCreate date: {self.create_date.strftime("%d.%m.%y")}' 

class TaskManager:
 
    def create_task(self, tasks):
        title = input('Write task title\n')
        text = input('Write task text\n')

        task = Task(title=title, text=text)
        tasks.append(task)

    def view_tasks(self, tasks):
        if tasks == []:
            print('No tasks')
        else:
            print(f'You have {len(tasks)} tasks:',
                  *[f'{i+1}:{task.title}' for i, task in enumerate(tasks)],
                  sep='\n')
        return len(tasks)

    def check_task(self, tasks):
        task_amount = self.view_tasks(tasks)
        if task_amount != 0:
            while True:
                task_id = input('Enter id of the task you want to view, or 0 if you want to return to the menu:\n')
                
                if task_id == '0':
                    break
                else: 
                    print(tasks[int(task_id)-1]) 


    def change_task_status(self, task:Task):
        status = input('Enter status:\n')
        task.status = status


