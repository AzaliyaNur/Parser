from os import lstat
from bs4 import BeautifulSoup
import requests
import pyodbc 
from datetime import datetime

cnxnBGU = pyodbc.connect("Driver={SQL Server Native Client 10.0};"
                            "Server=WIN-K1RC9U9RIIK\SQLS;"
                            "Database=BGU;"
                            "Trusted_Connection=yes;")
cursorBGU = cnxnBGU.cursor()



url = 'https://pk-inf.bashedu.ru/static/file_vault/БашГУ '
i = ['11.03.04_ФТИ_Электроника и наноэлектроника_О_Б.HTML',
'10.03.01_ИИГУ_Информационная безопасность_О_Б.HTML',
'01.03.01_ФМИТ_Математика_О_Б.HTML',
'02.03.01_ФМИТ_Математика и компьютерные науки_О_Б.HTML',
'02.03.03_ФМИТ_Математическое обеспечение и администрирование информационных систем_О_Б.HTML',
'28.03.03_ФТИ_Наноматериалы_О_Б.HTML',
'09.03.03_ФМИТ_Прикладная информатика_О_Б.HTML',
'01.03.02_ФМИТ_Прикладная математика и информатика_О_Б.HTML',
'03.03.01_ФТИ_Прикладные математика и физика_О_Б.HTML',
'15.03.02_ИНЖ_Технологические машины и оборудование_О_Б.HTML',
'11.03.02_ФТИ_Инфокоммуникационные технологии и системы связи_О_Б.HTML'
]



for k in i:
    requestDrop = ""
    requestDrop += 'DROP TABLE "'
    requestDrop += str(k)
    requestDrop += '"'
    cursorBGU.execute(requestDrop)
    print(requestDrop)



for k in i:
    temp_url = url + k
    print(k,temp_url)
    html = requests.get(temp_url)
    print(html)        
    soup = BeautifulSoup(html.text, 'html.parser')
    html.encoding = 'cp1251'
    htmlString = html.text

#Создаём таблицу

    requestCreate = 'CREATE TABLE "'
    requestCreate += str(k)
    requestCreate += '" (nomer integer,id varchar(200),summa INTEGER,summa1 INTEGER,ball1 integer,ball2 integer,ball3 INTEGER,ud INTEGER,sogl VARCHAR(200))'
    cursorBGU.execute(requestCreate)
    print(requestCreate)


    num_sogl    = 0
    str_cond    = []

    for supik in soup.find_all('tr', class_='R0'):
        if supik.find('td', class_ = 'R12C0') is not None:
            csv_str     = ""
            num_sogl    = 0
            str_cond.clear()
            for sup in supik.find_all('td', class_='R12C0'):
                
                sup_txt = sup.text
                
                num_sogl    = num_sogl + 1

                #В тексте много \n, так что их нужно "удалить" 
                    
                csv_str1    = ""
                csv_str1    += sup_txt.replace('\n', '')

                #создаём проверку позиции, с помощью обычного счёта переменной. таким образом и делаем всю работу

                if num_sogl == 2:
                    csv_str1     = "'" +csv_str1+ "'"
                else:
                    csv_str1     = csv_str1

                str_cond.append(csv_str1)

                #знак согласия весьма трудно читается, поэтому его нужно заменить на что-то простое

                if (num_sogl >= 9):
                    if str_cond[8]== '     â\x9c\x93    ':
                        print(str_cond[8])
                        csv_str1 = csv_str1.replace('     â\x9c\x93    ','1')
                        print(csv_str1)   
                    else:
                        csv_str1 =   '0'



                

                if csv_str1 == '':
                    csv_str1 = csv_str1.replace('','0')

                csv_str1    += ','
                csv_str     += csv_str1


            

            #убираем последний знак в строке

            l = len(csv_str)
            Removed_last = csv_str[:l-1]           
            
            print(Removed_last)

            requestInsert = 'INSERT INTO "'
            requestInsert += str(k)
            requestInsert += '" VALUES ('
            requestInsert += str(Removed_last)
            requestInsert += ");"
            print(requestInsert)
            cursorBGU.execute(requestInsert)
            
            
    



cnxnBGU.commit()
cnxnBGU.close()
            