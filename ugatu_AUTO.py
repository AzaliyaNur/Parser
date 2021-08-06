from os import lstat
from bs4 import BeautifulSoup
import requests
import csv
import pyodbc 
from datetime import datetime

#connect to server


cnxnUGATU = pyodbc.connect("Driver={SQL Server Native Client 10.0};"
                            "Server=WIN-K1RC9U9RIIK\SQLS;"
                            "Database=Ugatu;"
                            "Trusted_Connection=yes;")
cursorUGATU = cnxnUGATU.cursor()



template_url = 'https://www.ugatu.su/abitur/bachelor-and-specialist/admission-ratings/?institution=УГАТУ&funding=Бюджетная+основа&education_level=Бакалавриат&education_form=Очная&specialty='
#html = requests.get(url)
#soup = BeautifulSoup(html.text, 'html.parser')
i = [
'118',
'119',
'120',
'121',
'122',
'123',
'124',
'125',
'126',
'127',
'128',
'129',
'130',
'131',
'132',
'133',
'134',
'135',
'136',
'137',
'138',
'139',
'140',
'142',
'143',
'144',
'145',
'148',
'149',
'150',
'194',
'195',
'196',
'197',
'198',
'199',
'200',
'201',
'202'
]

a =[
'01.03.02 Прикладная математика и информатика',
'01.03.04 Прикладная математика',
'02.03.01 Математика и компьютерные науки',
'02.03.03 Математическое обеспечение и администрирование информационных систем',
'09.03.01 Информатика и вычислительная техника',
'09.03.02 Информационные системы и технологии',
'09.03.03 Прикладная информатика',
'09.03.04 Программная инженерия',
'10.03.01 Информационная безопасность',
'11.03.02 Инфокоммуникационные технологии и системы связи',
'11.03.04 Электроника и наноэлектроника',
'12.03.01 Приборостроение',
'12.03.04 Биотехнические системы и технологии',
'13.03.01 Теплоэнергетика и теплотехника',
'13.03.02 Электроэнергетика и электротехника',
'13.03.03 Энергетическое машиностроение',
'15.03.01 Машиностроение',
'15.03.02 Технологические машины и оборудование',
'15.03.04 Автоматизация технологических процессов и производств',
'15.03.05 Конструкторско-технологическое обеспечение машиностроительных производств',
'15.03.06 Мехатроника и робототехника',
'20.03.01 Техносферная безопасность',
'22.03.01 Материаловедение и технологии материалов',
'24.03.04 Авиастроение',
'24.03.05 Двигатели летательных аппаратов',
'25.03.01 Техническая эксплуатация летательных аппаратов и двигателей',
'27.03.01 Стандартизация и метрология',
'27.03.04 Управление в технических системах',
'27.03.05 Инноватика',
'28.03.02 Наноинженерия',
'10.05.05 Безопасность информационных технологий в правоохранительной сфере',
'11.05.04 Инфокоммуникационные технологии и системы специальной связи',
'13.05.02 Специальные электромеханические системы',
'15.05.01 Проектирование технологических машин и комплексов',
'20.05.01 Пожарная безопасность',
'23.05.01 Наземные транспортно-технологические средства',
'24.05.02 Проектирование авиационных и ракетных двигателей',
'24.05.06 Системы управления летательными аппаратами',
'27.05.01 Специальные организационно-технические системы'
]

#делаем дроп, если уже существуют таблицы

#for b in a:
    #requestDrop = ""
    #requestDrop += 'DROP TABLE "'
    #requestDrop += str(b)
    #requestDrop += '"'
    #cursorUGATU.execute(requestDrop)
    #print(requestDrop)


for k in i:
    print(k)
    #задаем адрес
    #url = template_url + i[k]
    url = template_url + k
    print(url)

    #качаем сайт
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')

    head_csv = ""
    #---------
    for t_data in soup.find_all('div'):
        lt = []
        for tb_data in t_data.find_all('h4'):
            head_csv = tb_data
    #---------
    head_num    = 0
    head_num    = head_csv.string.find(',')
    head_csv   = head_csv.string[0:head_num]
    head_csv   = head_csv

#создаём таблицу
    requestCreate = 'CREATE TABLE "'
    requestCreate += str(head_csv)
    requestCreate += '" (id VARCHAR(200),ball INTEGER,ball1 INTEGER,ball2 INTEGER,ball3 INTEGER,ud INTEGER,sogl VARCHAR(200))'
    cursorUGATU.execute(requestCreate)
    print(requestCreate)


    #парсим
    arr = []
    arr_num = 0
    

    for t_data in soup.find_all('table'):
        lt = []
        for tb_data in t_data.find_all('tbody'):
            for data in tb_data.find_all('tr'): #Находим все данные из таблицы
                csv_str = ""
                csv_str += "'"+data.find_all('td')[2].text+"'"
                csv_str += ","
                csv_str += data.find_all('td')[3].text
                csv_str += ","
                csv_str += data.find_all('td')[4].text
                csv_str += ","
                csv_str += data.find_all('td')[5].text
                csv_str += ","
                csv_str += data.find_all('td')[6].text
                csv_str += ","
                csv_str += data.find_all('td')[7].text
                csv_str += ","
                csv_str += data.find_all('td')[8].text 
                if csv_str.find('Да'):
                    csv_str = csv_str.replace('Да', "'"+'Yes'+"'")
                if csv_str.find('Нет'):
                    csv_str = csv_str.replace('Нет', "'"+'No'+"'")
                if csv_str.find('На другой специальности'):
                    csv_str = csv_str.replace('На другой специальности', "'"+'On another specialty'+"'")
                # 
                lt.append(csv_str)
        arr.append(lt)
        arr_num = arr_num + 1
                #print(csv_str)
    if arr_num > 0:
        for str1 in arr[arr_num-1]:
            print(str1)
            #заполняем таблицу
            requestInsert = 'INSERT INTO "'
            requestInsert += str(head_csv)
            requestInsert += '" VALUES ('
            requestInsert += str1
            requestInsert += ");"
            print(requestInsert)
            cursorUGATU.execute(requestInsert)  

cnxnUGATU.commit()
cnxnUGATU.close()


