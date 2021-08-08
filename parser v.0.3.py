from os import lstat
from bs4 import BeautifulSoup
import requests
import pyodbc 
from datetime import datetime


def MakeUrl(k,url):
            
    temp_url = url + k
    html = requests.get(temp_url)  
    soup = BeautifulSoup(html.text, 'html.parser')    
    return soup 

def Update(k,str_cond): 
    com = 'UPDATE "'+str(k)+'" SET sogl = '+"'"+str(str_cond[1])+"'"+" WHERE id = "+str(str_cond[0])
    return com

def Select(k):
    com = 'SELECT id FROM "'+str(k)+'" WHERE sogl ='+"'Yes'"
    return com

def Delete(i,row):
    com =  'delete from "'+str(i)+'" where id = '+"'"+row[0]+"'"
    return com

def Delete_NO(i,row):
    com =  'delete from "'+str(i)+'" where id = '+"'"+row[0]+"'"+"and sogl = 'No'"
    return com

#--------------------------------------------------------------------------------------------#   

def CreateTable(k,i):
    k += str(i)
    com = 'CREATE TABLE "'+k+'" (id VARCHAR(200), ball INTEGER, sogl VARCHAR(200))'
    return com

def Select_(k,i):
    com = 'SELECT id,ball,sogl FROM "'+k+'" WHERE sogl = '+"'"+str(i)+"'"
    return com

def Insert_Into(k,row,i):
    k += str(i)
    com = 'INSERT INTO "'+k+'" VALUES ('+"'"+str(row[0])+"'"+','+str(row[1])+','+"'"+str(row[2])+"')"
    return com

def Drop(k,i):
    k += str(i)
    com = 'DROP TABLE "'+k+'"'
    return com

def AllNo(k):
    #TableDelete = Drop(k,2)
    TableCreate = CreateTable(k,2)
    #cursorNO.executemany(TableDelete)   
    cursorNO.execute(TableCreate)
    select_no = Select_(k,'No')
    return select_no

def AllYes(k):
    #TableDelete = Drop(k,1)
    TableCreate = CreateTable(k,1)
    #cursorYES.execute(TableDelete) 
    cursorYES.execute(TableCreate) 
    select_yes = Select_(k,'Yes')
    return select_yes
    

 
    

cnxnBGU = pyodbc.connect("Driver={SQL Server Native Client 10.0};"
                                "Server=WIN-K1RC9U9RIIK\SQLS;"
                                "Database=BGU;"
                                "Trusted_Connection=yes;")
cursorBGU = cnxnBGU.cursor()
      
cnxnUGATU = pyodbc.connect("Driver={SQL Server Native Client 10.0};"
                                    "Server=WIN-K1RC9U9RIIK\SQLS;"
                                    "Database=Ugatu;"
                                    "Trusted_Connection=yes;")
cursorUGATU = cnxnUGATU.cursor()

cnxnUGNTU = pyodbc.connect("Driver={SQL Server Native Client 10.0};"
                            "Server=WIN-K1RC9U9RIIK\SQLS;"
                            "Database=UGNTU;"
                            "Trusted_Connection=yes;")
cursorUGNTU = cnxnUGNTU.cursor()
        
cnxnYES = pyodbc.connect("Driver={SQL Server Native Client 10.0};"
                            "Server=WIN-K1RC9U9RIIK\SQLS;"
                            "Database=YES;"
                            "Trusted_Connection=yes;")
cursorYES = cnxnYES.cursor()

cnxnNO = pyodbc.connect("Driver={SQL Server Native Client 10.0};"
                            "Server=WIN-K1RC9U9RIIK\SQLS;"
                            "Database=NO;"
                            "Trusted_Connection=yes;")
cursorNO = cnxnNO.cursor()
   

class BGU:       
    def __init__(self):
        return

    def statistic(tables):

        return
    
    def main(self): 
        tablesBGU = ['11.03.04_ФТИ_Электроника и наноэлектроника_О_Б.HTML',
                    '10.03.01_ИИГУ_Информационная безопасность_О_Б.HTML',
                    '01.03.01_ФМИТ_Математика_О_Б.HTML',
                    '02.03.01_ФМИТ_Математика и компьютерные науки_О_Б.HTML',
                    '02.03.03_ФМИТ_Математическое обеспечение и администрирование информационных систем_О_Б.HTML',
                    '28.03.03_ФТИ_Наноматериалы_О_Б.HTML',
                    '09.03.03_ФМИТ_Прикладная информатика_О_Б.HTML',
                    '01.03.02_ФМИТ_Прикладная математика и информатика_О_Б.HTML',
                    '03.03.01_ФТИ_Прикладные математика и физика_О_Б.HTML',
                    '15.03.02_ИНЖ_Технологические машины и оборудование_О_Б.HTML',
                    '11.03.02_ФТИ_Инфокоммуникационные технологии и системы связи_О_Б.HTML']


        for k in tablesBGU:
            soup = MakeUrl(k,'https://pk-inf.bashedu.ru/static/file_vault/БашГУ ')

            for supik in soup.find_all('tr', class_='R0'):

                if supik.find('td', class_ = 'R12C0') is not None:
                    num_sogl    = 0           
                    str_cond = []
                    str_cond.clear()
                    
                    for sup in supik.find_all('td', class_='R12C0'):
                        sup_txt = sup.text
                        num_sogl = num_sogl + 1

                                #В тексте много \n, так что их нужно "удалить"                         
                        csv_str1    = ""
                        csv_str1    += sup_txt.replace('\n', '')

                                #создаём проверку позиции, с помощью обычного счёта переменной. таким образом и делаем всю работу
                        if num_sogl == 2:
                            csv_str1     = "'" +csv_str1+ "'"
                            str_cond.append(csv_str1)
                        if (num_sogl >= 9):
                            if csv_str1 != '': 
                                if csv_str1.find('â\x9c\x93') != -1:
                                    csv_str1 = 'Yes'
                                    #csv_str1 = csv_str1.replace('â\x9c\x93','Yes')                          
                                    str_cond.append(csv_str1)   
                            else:
                                csv_str1 = 'No'
                                str_cond.append(csv_str1)
                    request = Update(k,str_cond)
                    cursorBGU.execute(request)
        cnxnBGU.commit()

class UGATU:
    def __init__(self):
        return 
    def main(self):

        irl = ['118','119','120','121','122','123','124','125','126','127','128','129','130','131','132','133','134','135','136',
        '137','138','139','140','142','143','144','145','148','149','150','194','195','196','197','198','199','200','201','202']
    
        for k in irl:
            soup = MakeUrl(k,'https://www.ugatu.su/abitur/bachelor-and-specialist/admission-ratings/?institution=УГАТУ&funding=Бюджетная+основа&education_level=Бакалавриат&education_form=Очная&specialty=')

            head_csv = ""

            #---------
            for t_data in soup.find_all('div'):

                for tb_data in t_data.find_all('h4'):
                    head_csv = tb_data
            #---------
            head_num    = 0
            head_num    = head_csv.string.find(',')
            head_csv   = head_csv.string[0:head_num]
            head_csv   = head_csv

            #парсим
            
            for t_data in soup.find_all('table'):
                for tb_data in t_data.find_all('tbody'):

                    for data in tb_data.find_all('tr'): #Находим все данные из таблицы
                        str_cond = []
                        str_cond.clear()

                        str_id     = "'"+data.find_all('td')[2].text+"'" 
                        str_sogl   = data.find_all('td')[8].text      
                        str_cond.append(str_id)
                                        
                        str_sogl = str_sogl.replace('Да', 'Yes')
                        str_sogl = str_sogl.replace('Нет', 'No')
                        str_sogl = str_sogl.replace('На другой специальности', 'On another specialty')

                        str_cond.append(str_sogl)              

                        text = Update(head_csv,str_cond)
                        cursorUGATU.execute(text)
        cnxnUGATU.commit() 

class UGNTU:
    def __init__(self):
        return
    def main(self):

        tableUrls = ['https://ams.rusoil.net/abitonline/onlinepeople.php?id=1',
        'https://ams.rusoil.net/abitonline/onlinepeople.php?id=109',
        'https://ams.rusoil.net/abitonline/onlinepeople.php?EduOsn=1&id=59',
        'https://ams.rusoil.net/abitonline/onlinepeople.php?EduOsn=1&id=115' ]

        for template_url in tableUrls:

            #задаем адрес
            url = template_url
                    
            #качаем сайт
            html = requests.get(url)
            soup = BeautifulSoup(html.text, 'html.parser')
            #---------
            #названия таблиц
            for t_data in soup.find('b'):
                head_table = str(t_data)
            for data in soup.find_all('tr'):
                if data.text !='\n\n':
                    dat_str = ''
                    num = 0 
                    str_cond = []
                    str_cond.clear()
                    if data.find('th') is None:
                        for dat in data.find_all('td'):
                            dat_str0 = dat.text                            
                            num = num + 1
                                
                            if num == 2: 
                                id_list = list(dat_str0)
                                if id_list[0]=='I':
                                    str_cond.append("'"+'0'+"'")
                                else:
                                    id_list.pop(0)
                                    id_list.pop(0)
                                    if len(id_list)<11:
                                        str_cond.append("'"+'0'+"'")
                                    else:
                                        dat_str0 = "'"+str(id_list[0])+str(id_list[1])+str(id_list[2])+'-'+str(id_list[3])+str(id_list[4])+str(id_list[5])+'-'+str(id_list[6])+str(id_list[7])+str(id_list[8])+' '+str(id_list[9])+str(id_list[10])+"'"
                                        str_cond.append(dat_str0)
                            if num ==9:
                                dat_str0 = dat_str0.replace('\r\n\tДа','Yes')                    
                                dat_str0 = dat_str0.replace('\r\n\tНа другой','In other')
                                dat_str0 = dat_str0.replace('\n','No')
                                str_cond.append(dat_str0)
                            dat_str += dat_str0
                        requestUgntu = Update(head_table,str_cond)
                        cursorUGNTU.execute(requestUgntu)
        cnxnUGNTU.commit()



class Filter:
    def __init__(self):
        return
    def main(self):
        tablesUgatu = ['01.03.02 Прикладная математика и информатика',
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

        tablesUgatu_sogl = ['01.03.02 Прикладная математика и информатика',
        '09.03.03 Прикладная информатика',
        '11.03.02 Инфокоммуникационные технологии и системы связи',
        '27.03.05 Инноватика',
        '27.03.04 Управление в технических системах',
        '09.03.02 Информационные системы и технологии',
        '09.03.01 Информатика и вычислительная техника',
        '15.03.06 Мехатроника и робототехника',
        '11.03.04 Электроника и наноэлектроника']

        tablesBGU = ['11.03.04_ФТИ_Электроника и наноэлектроника_О_Б.HTML',
            '10.03.01_ИИГУ_Информационная безопасность_О_Б.HTML',
            '01.03.01_ФМИТ_Математика_О_Б.HTML',
            '02.03.01_ФМИТ_Математика и компьютерные науки_О_Б.HTML',
            '02.03.03_ФМИТ_Математическое обеспечение и администрирование информационных систем_О_Б.HTML',
            '28.03.03_ФТИ_Наноматериалы_О_Б.HTML',
            '09.03.03_ФМИТ_Прикладная информатика_О_Б.HTML',
            '01.03.02_ФМИТ_Прикладная математика и информатика_О_Б.HTML',
            '03.03.01_ФТИ_Прикладные математика и физика_О_Б.HTML',
            '15.03.02_ИНЖ_Технологические машины и оборудование_О_Б.HTML',
            '11.03.02_ФТИ_Инфокоммуникационные технологии и системы связи_О_Б.HTML']
        
        tablesBGU_sogl = ['02.03.01_ФМИТ_Математика и компьютерные науки_О_Б.HTML',
        '02.03.03_ФМИТ_Математическое обеспечение и администрирование информационных систем_О_Б.HTML',
        '09.03.03_ФМИТ_Прикладная информатика_О_Б.HTML',
        '01.03.02_ФМИТ_Прикладная математика и информатика_О_Б.HTML',
        '11.03.04_ФТИ_Электроника и наноэлектроника_О_Б.HTML']

        tablesUgntu = ['Списки поступающих: БАГ БАГ Автоматизация технологических процессов и производств (в нефтяной и газовой промышленности) (г. Уфа)',
                    'Списки поступающих: БАТ БАТ Автоматизация технологических процессов и производств (в нефтепереработке и нефтехимии) (г. Уфа)',
                    'Списки поступающих: БИФ БИФ Прикладная информатика в экономике и финансах ТЭК (г. Уфа)',
                    'Списки поступающих: БПО БПО Программное обеспечение средств вычислительной техники и автоматизированных систем (г. Уфа)']

       
            #те, кто подал заявление в бгу, удаляются из угату
                   
        for k in tablesBGU: 
            requestBGU = Select(k)
            cursorBGU.execute(requestBGU)
                
            for row in cursorBGU:  
                for i in tablesUgatu:                       
                    requestUgatu = Delete(i,row)                       
                    cursorUGATU.execute(requestUgatu)
                        
            
            #удаляем тех, кто подал согласие в Угату, из БГУ

        for k in tablesUgatu: 
            requestUgatu = Select(k)
            cursorUGATU.execute(requestUgatu)

            for row in cursorUGATU:                      
                for i in tablesBGU:                       
                    requestBGU = Delete(i,row)
                    cursorBGU.execute(requestBGU)
                        

            #удаляем тех, кто уже подал заявление, с других специальностей Угату
           
        for k in tablesUgatu:
            requestUgatu = Select(k)
            cursorUGATU.execute(requestUgatu)

            for row in cursorUGATU.fetchall():                   
                for i in tablesUgatu:
                    requestUgatu_1 = Delete_NO(i,row)                       
                    cursorUGATU.execute(requestUgatu_1)
                        

            #Удаляем из списков угату всех, кто "На другом специальности"
           

        for i in tablesUgatu:
            requestUgatu +='delete from "'+i+'" where sogl  = '+"'On another specialty'"
            cursorUGATU.execute(requestUgatu)


            #те, кто подал заявление в бгу на одном направлении, удаляются из других

        for k in tablesBGU:
            requestBGU = Select(k)
            cursorBGU.execute(requestBGU)

            for row in cursorBGU.fetchall():                   
                for i in tablesBGU:
                    requestBGU_1 = Delete_NO(i,row)
                    cursorBGU.execute(requestBGU_1)

            #Удалить всех из Угату и Бгу, кто подал заявление в УГНТУ#

            for k in tablesUgntu:
                requestUgntu = Select(k)
                cursorUGNTU.execute(requestUgntu)
    
                for row in cursorUGNTU.fetchall():  

                    for i in tablesBGU:
                        requestBGU_1 = Delete_NO(i,row)
                        cursorBGU.execute(requestBGU_1)
                        
                    for i in tablesUgatu:
                        requestUgatu_1 = Delete_NO(i,row)
                        cursorUGATU.execute(requestUgatu_1)

#создание и заполнение таблиц с согласиями и без из угату и бгу


        for k in tablesUgatu_sogl:
            cursorUGATU.execute(AllYes(k))
            for row in cursorUGATU.fetchall():
                insert = Insert_Into(k,row,1)
                cursorYES.execute(insert)
            cursorUGATU.execute(AllNo(k))
            for row in cursorUGATU.fetchall():
                insert1 = Insert_Into(k,row,2)
                cursorNO.execute(insert1)


        for k in tablesBGU_sogl:
            cursorBGU.execute(AllYes(k))
            for row in cursorBGU.fetchall():
                insert = Insert_Into(k,row,1)
                cursorYES.execute(insert)
            cursorBGU.execute(AllNo(k))
            for row in cursorBGU.fetchall():
                insert1 = Insert_Into(k,row,2)
                cursorNO.execute(insert1)


        cnxnUGNTU.commit()
        cnxnUGNTU.close() 

        cnxnBGU.commit()
        cnxnBGU.close()

        cnxnUGATU.commit()
        cnxnUGATU.close() 

        cnxnYES.commit()
        cnxnYES.close()

        cnxnNO.commit()
        cnxnNO.close()
                    
                
Bgu = BGU()  
Bgu_1= Bgu.main()  

Ugatu = UGATU()
ugatu_1 = Ugatu.main()

Ugntu = UGNTU()
Ugntu_1 = Ugntu.main()

Filt = Filter()
Filt_1 = Filt.main()




           









    

    

