from bs4 import BeautifulSoup # библиотека Python для извлечения данных из файлов HTML и XML
import requests

Template = "http://biik.ru/rasp/cg109.htm" # Запрос на сайт Биик Сибгути
a = requests.get(Template) # получение запроса
a.encoding="windows-1251" # кодировка
print(a.text) # вывод на экран
if a == 404: # если ошибка
	print ('Not Found')
else: 
	html_code = a.text
	bs =BeautifulSoup(html_code,"html.parser") #парсинг html документа
	Lesson = bs.findAll('td') # td - столбец
	
	file = open ("Timetable.txt", "w") # запись в файл
	for item in Lesson:
		file.write(item.text +"\n")
	file.close()

	line = open ("Timetable.txt").readlines()
	for i in range(104):
		line.pop(0)
	
	f = open ("Timetable.txt", "w")
	for i in line:
		f.write(i)
	f.close()