from task import Task

class User:

    def __init__(self, name, password) -> None:
        self.name = name 
        self.password = password
        self.tasks: list[Task] = list()

    def __str__(self) -> str:
        return f'Name: {self.name}'

class UserManager:
    _user_list: list[User] = list() 

    @staticmethod
    def load_users() -> list[User]:
        return UserManager._user_list

    @staticmethod
    def save_user(user: User):
        UserManager._user_list.append(user)

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


