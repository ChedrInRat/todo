import socket, threading
from user import User, UserManager
from task import TaskManager

def create_user(client:socket.socket):
    client.send('Hi, you need create user!\nEnter name: '.encode('utf-8'))
    name = client.recv(1024).decode('utf-8')
    client.send('Enter password: '.encode('utf-8'))
    password = client.recv(1024).decode('utf-8')
    UserManager.create_user(name=name, password=password)


def login_user(client:socket.socket) -> User|None:
    users_list = UserManager.load_users 

    msg_menu = 'System have this users:\n'  
    for key, name in enumerate(users_list()):
        msg_menu += f'{key+1}: {name}\n'
    msg_menu += 'new -> create new user\n0 -> exit'
    client.send(msg_menu.encode('utf-8'))

    action = client.recv(1024).decode('utf-8')
    if action == 'new':
        create_user(client)
        return login_user(client)

    elif 0 < int(action) <= len(users_list()):
        uid = int(action) - 1
        client.send('Enter password: '.encode('utf-8'))
        password = client.recv(1024).decode('utf-8')
        if user := UserManager.user_login(uid=uid, password=password):
            return user
    
def menu(client:socket.socket, user:User):
    client.send(f'Hi, {user.name}\n'.encode('utf-8'))
    while True:
        msg_menu = 'Select action:\n0 -> exit\n1 -> create task\n2 -> view task\n3 -> check task'
        client.send(msg_menu.encode('utf-8'))
        
        tm = TaskManager(user=user, client=client)
        actions: dict = {'1': tm.create_task, '2': tm.view_tasks, '3': tm.check_task}
        
        action = client.recv(1024).decode('utf-8')

        if action == '0':
            break
        else:
            actions[action]()

def handle_client(client:socket.socket, addr):
    print(f'Client {addr} connect')
    users_list = UserManager.load_users
    while True:
        if not users_list():
            create_user(client)
        else:
            if user := login_user(client):
               menu(client, user) 
            else:
                break
    client.close()


def main():
    while True:
        client, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(client, addr))
        thread.start() 

if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 8080))
    server.listen(5)

    main()
