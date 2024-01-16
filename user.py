
class User:

    def __init__(self, name, password) -> None:
        self.name = name 
        self.password = password
        self.tasks_path = f'{name}.txt'

    def __str__(self) -> str:
        return f'Name: {self.name}'
    

class UserManager:
    path = 'users.txt'
    _user_list: list[User] = list() 

    @staticmethod
    def load_users() -> list[User]:
        users = list()
        lines = list()
        try:
            with open(UserManager.path, 'r') as f:
                lines = f.readlines()
        except:
            pass

        if lines:
            for line in lines:
                name, password, _ = [x.split(':')[-1] for x in line.strip().split(',')] 
                user = User(name=name, password=password)
                
                users.append(user)

        return users 

    @staticmethod
    def save_user(user: User):
        user_dict = user.__dict__
        with open(UserManager.path, 'a+') as f:
            f.write(','.join([f'{key}:{user_dict[key]}' for key in user_dict]) + '\n')

    @staticmethod
    def create_user():
        name = input('Enter you name: ')
        password = input('Enter password: ')
        user = User(name=name, password=password)

        UserManager.save_user(user=user)

        return user 

    @staticmethod
    def user_login(uid) -> bool:
        users = UserManager.load_users() 
        user = users[uid]
        password = input('Enter password: ') 
        
        return password == user.password

