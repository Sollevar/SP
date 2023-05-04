import socket
import ssl
def receive(sock): # функция читает данные из сокета
    data=b''
    while True:
        part=sock.recv(1024)
        data += part
        if len(part)<1024:
            break
    return data.decode()

 
def list_messages(sock): # функция показа списка сообщений
    sock.send("LIST\r\n".encode())
    msg_list = receive(sock)
    print(msg_list)
    print('Нажмите 1 чтобы вывести все сообщения в столбец')
    
def download_message(sock, msg_num): # функция скачивания сообщений
    sock.send("RETR {}\r\n".format(msg_num).encode())
    msg_data = receive(sock)
    with open('message{}.txt'.format(msg_num), 'w', encoding='utf-8') as f:
        f.write(msg_data)
    print('Еще раз выполните данную команду с номером скаченного сообщения')
    

def pop3_client(): # основная функция
    # Подключение к серверу
    context = ssl.create_default_context() # SSL кодировка
    sock = context.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM), server_hostname='pop.mail.ru')
    sock.connect(('pop.mail.ru', 995))
    print(receive(sock))
    print('Соединение установлено')

    #Аутентификация на сервере
    user=input('User: ')
    sock.send("USER {}\r\n".format(user).encode())
    print(receive(sock))

    password = input('Password: ')
    sock.send("PASS {}\r\n".format(password).encode())
    print(receive(sock))

    while True: # меню
        # Показать список сообщений или скачать сообщение
        action = input('Choose an action: 1 - Список сообщений, 2 - Скачивание сообщения, 3 - Выход\n')
        if action == '1':
            list_messages(sock)
        elif action == '2':
            msg_num = input('Message number: ')
            download_message(sock, msg_num)
        elif action == '3':
            break
        else:
            print('Invalid action')

    # Завершение сессии
    sock.send("QUIT\r\n".encode())
    print(receive(sock))
    sock.close()

if __name__ == '__main__':
    pop3_client()
