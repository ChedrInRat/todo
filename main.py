from user import User, UserHandler, UserManager
from task import TaskManager


def menu(user: User):
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
            tm = TaskManager(user)
            # '3': tm.check_task}
            actions: dict = {'1': tm.create_task, '2': tm.view_tasks, }

            actions[action]()


def main():

    while True:
        if not (user_list := UserHandler.get_list()):
            print('Hi, you need create user!\n')
            UserManager.create_user()
        else:
            print('System have this users:',
                  *[f'{uid+1}: {user.name}' for uid,
                      user in enumerate(user_list)],
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
                user = user_list[uid]
                if UserManager.login_user(user):
                    menu(user)
                else:
                    print('Bad login')


if __name__ == '__main__':
    main()
