from user import User, UserManager
from task import TaskManager

def menu(user:User):
    print(f'Hi, {user.name}!')
    while True: 
        print('Select action:',
              '0 -> exit',
              '1 -> create task',
              '2 -> view tasks',
              '3 -> check task',
              sep='\n')

        action = input()
        if action == '0':
            break
        else:
            tm = TaskManager()
            actions: dict = {'1': tm.create_task, '2': tm.view_tasks, '3': tm.check_task}

            actions[action](user.tasks) 

def main():
    user_list = UserManager.load_users

    while True:
        if not user_list():
            print('Hi, you need create user!\n')
            UserManager.create_user()
        else:
            print('System have this users:',
                  *[f'{uid+1}: {user.name}' for uid, user in enumerate(user_list())],
                  'new -> create new user',
                  '0 -> exit',
                  sep='\n')
            
            action = input()
            
            if action == '0':
                break
            elif action == 'new':
                UserManager.create_user()
            else:
                uid = int(action) - 1
                if UserManager.user_login(uid=uid):
                    menu(user_list()[uid])
                else:
                    print('Bad login')


if __name__ == '__main__':
    main()
