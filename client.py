import socket
import threading

nickname = input("Choose a nickname : ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))

            else:
                print(message)
        except:
            print("An Error Occured")
            client.close()
            break


def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

# admin levels normal user and admin
# to add features kick and ban users from chat room
