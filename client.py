import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    client.connect(('0.0.0.0', 8080))
    print('Connected')

    while True:
        data = client.recv(1024)
        response = data.decode('utf-8')
        if not response:
            break
        print(response)
        msg = input()
        client.send(msg.encode('utf-8'))

    client.close()

if __name__ == '__main__':
    main()
