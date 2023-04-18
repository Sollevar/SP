from ftplib import FTP # библиотека для работы с FTP
import os
server = str(input("ip addres: ")) # адрес сервера
username = str(input("username: ")) # имя пользователя
password = str(input("password: ")) # пароль
try: # получение соединения
    ftp = FTP(server)
    ftp.login(username,password)
    print("Соединение установлено")
    mainfunction()
except: # ошибка
    print("Ошибка соединения с сервером")

def mainfunction():
   gap=-1
   while gap!=0: # меню действий
     print("1.Вывести список файлов")
     print("2.Загрузить файл на сервер")
     print("3.Скачать файл с сервера")
     print("4.Выход")
     gap = int(input("Выбирите действие"))
     if gap == 1:
       print(ftp.retrlines('LIST')) # вывод списка файлов на сервере
     elif gap == 2:
       file = str(input('Какой файл загружаем на сервер: '))
       file_to_upload = open(file, 'rb')
       ftp.storbinaty('STOR' + os.path.basename(file),file_to_upload) # загрузка файла на сервер
       print("файл отправлен и загружен на сервер")
     elif gap == 3:
       print(ftp.retrlines('LIST'))
       file = str(input('Какой файл скачаем с сервера: '))
       dir = open('/home/igor/SP/SP/Lab5/' + file, 'wb') # загрузка файла с сервера в папку
       with open(dir+"\\"+file, 'wb') as a:
           ftp.retbinary('RETR' + file, a.write)
       print("файл получен")
     elif gap == 4: # выход
       return
     else:
       print("нет такого действия")
       mainfunction()
   ftp.close