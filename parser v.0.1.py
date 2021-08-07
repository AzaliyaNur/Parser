from os import lstat
from bs4 import BeautifulSoup
import requests
import pyodbc 
from datetime import datetime

class BGU_DB:
    def Connect(self):
        self.cnxnBGU = pyodbc.connect("Driver={SQL Server Native Client 10.0};"
                                "Server=WIN-K1RC9U9RIIK\SQLS;"
                                "Database=BGU;"
                                "Trusted_Connection=yes;")
        self.cursorBGU = self.cnxnBGU.cursor()
    def Exe(self,requestUpd):
        self.cursorBGU.execute(requestUpd)
    def ExeBGU(self,requestBGU):
        self.cursorBGU.execute(requestBGU)
    def Exe_1(self,requestBGU_1):
        self.cursorBGU.execute(requestBGU_1)
    def CLOSE(self):
        self.cnxnBGU.commit()
        self.cnxnBGU.close()

class UGATU_DB:
    def Connect(self):
        self.cnxnUGATU = pyodbc.connect("Driver={SQL Server Native Client 10.0};"
                                        "Server=WIN-K1RC9U9RIIK\SQLS;"
                                        "Database=Ugatu;"
                                        "Trusted_Connection=yes;")
        self.cursorUGATU = self.cnxnUGATU.cursor()
    def Exe(self,text):
        self.cursorUGATU.execute(text)
    def ExeUGATU(self,requestUgatu):
        self.cursorUGATU.execute(requestUgatu)
    def Exe_1(self,requestUgatu_1):
        self.cursorUGATU.execute(requestUgatu_1)
    def CLOSE(self):
        self.cnxnUGATU.commit()
        self.cnxnUGATU.close()

class UGNTU_DB:
    def Connect(self):
        self.cnxnUGNTU = pyodbc.connect("Driver={SQL Server Native Client 10.0};"
                                    "Server=WIN-K1RC9U9RIIK\SQLS;"
                                    "Database=UGNTU;"
                                    "Trusted_Connection=yes;")
        self.cursorUGNTU = self.cnxnUGNTU.cursor()
    def Exe(self,requestIns):
        self.cursorUGNTU.execute(requestIns)
    def ExeUGNTU(self,requestUgntu):
        self.cursorUGNTU.execute(requestUgntu)
    def CLOSE(self):
        self.cnxnUGNTU.commit()
        self.cnxnUGNTU.close()


class UGATU:
    def __init__(self):
        return 0
    def main(self):
        UGATU_DB.Connect
        template_url = 'https://www.ugatu.su/abitur/bachelor-and-specialist/admission-ratings/?institution=УГАТУ&funding=Бюджетная+основа&education_level=Бакалавриат&education_form=Очная&specialty='
        #html = requests.get(url)
        #soup = BeautifulSoup(html.text, 'html.parser')
        irl = [
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

            
        for k in irl:

            #задаем адрес
            url = template_url + k
            
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

            #парсим
            arr = []
            arr_num = 0
            

            for t_data in soup.find_all('table'):
                for tb_data in t_data.find_all('tbody'):

                    for data in tb_data.find_all('tr'): #Находим все данные из таблицы
                        str_com = []
                        str_com.clear()
                        str_sogl    = ""
                        str_id      = ""
                        csv_str     = ""
                        str_id     += "'"+data.find_all('td')[2].text+"'" 
                        str_sogl    = data.find_all('td')[8].text      

                        """if csv_str.find('Да'):
                            csv_str = csv_str.replace('Да', "'"+'Yes'+"'")
                        if csv_str.find('Нет'):
                            csv_str = csv_str.replace('Нет', "'"+'No'+"'")
                        if csv_str.find('На другой специальности'):
                            csv_str = csv_str.replace('На другой специальности', "'"+'On another specialty'+"'")"""   
                    
                        str_sogl = str_sogl.replace('Да', "'"+'Yes'+"'")
                        str_sogl = str_sogl.replace('Нет', "'"+'No'+"'")
                        str_sogl = str_sogl.replace('На другой специальности', "'"+'On another specialty'+"'")

                        csv_str += str_id + "," +str_sogl
                        str_com.append(csv_str)

                        
                        text = ""
                        text += 'UPDATE "'
                        text += head_csv
                        text += '" SET sogl = '
                        text += str_sogl
                        text +=  " WHERE id = "
                        text += str_id + ""
                        UGATU_DB.Exe

        UGATU_DB.CLOSE


class BGU:
    def __init__(self):
        return 0
    def main(self):
        BGU_DB.Connect

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
                    '11.03.02_ФТИ_Инфокоммуникационные технологии и системы связи_О_Б.HTML'
                    ]

        url = 'https://pk-inf.bashedu.ru/static/file_vault/БашГУ '

        for k in tablesBGU:
            temp_url = url + k
            html = requests.get(temp_url)      
            soup = BeautifulSoup(html.text, 'html.parser')

            for supik in soup.find_all('tr', class_='R0'):
                if supik.find('td', class_ = 'R12C0') is not None:
                    num_sogl    = 0
                    str_cond    = []
                    csv_str  = ""                
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
                        else:
                            csv_str1     = csv_str1
                        str_cond.append(csv_str1)

                        #знак согласия весьма трудно читается, поэтому его нужно заменить на что-то простое
                        if (num_sogl >= 9):
                            if str_cond[8]!= '': 
                                str_cond[8] = str_cond[8].replace('     â\x9c\x93    ','1')                          
                                csv_str1 = csv_str1.replace('     â\x9c\x93    ','1')    
                            else:
                                str_cond[8] ='0'
                                csv_str1 =   '0'

                        if csv_str1 == '':
                            csv_str1 = csv_str1.replace('','0')
                                
                        csv_str1 += ','
                        csv_str += csv_str1

                    l = len(csv_str)
                    Removed_last = csv_str[:l-1] 
                    


                    requestUpd = ""
                    requestUpd += 'UPDATE "'
                    requestUpd += str(k)
                    requestUpd += '" SET sogl = '
                    requestUpd += str(str_cond[8])
                    requestUpd +=  " WHERE id = "
                    requestUpd += str(str_cond[1])
                    BGU_DB.Exe

        BGU_DB.CLOSE

class UGNTU:
    def __init__(self):
        return 0
    def main(self):
        UGNTU_DB.Connect

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
                    num = 0 
                    dat_str = ""
                    str_cond = []
                    str_cond.clear()
                    if data.find('th') is None:
                        for dat in data.find_all('td'):
                            dat_str0 = dat.text
                            
                            num = num + 1
                            
                            if num == 2: 
                                id_list = list(dat_str0)
                                if id_list[0]=='I':
                                    str_cond.append('None')
                                else:
                                    id_list.pop(0)
                                    id_list.pop(0)
                                    if len(id_list)<11:
                                        str_cond.append('None')
                                    else:
                                        dat_str0 = str(id_list[0])+str(id_list[1])+str(id_list[2])+'-'+str(id_list[3])+str(id_list[4])+str(id_list[5])+'-'+str(id_list[6])+str(id_list[7])+str(id_list[8])+' '+str(id_list[9])+str(id_list[10])
                                        str_cond.append(dat_str0)
                            if num == 4:
                                if dat_str0 == 'Без вступительных':
                                    str_cond.append('0')
                                str_cond.append(dat_str0)
                            if num ==9:
                                dat_str0 = dat_str0.replace('\r\n\tДа','Yes')                    
                                dat_str0 = dat_str0.replace('\r\n\tНа другой','In other')
                                dat_str0 = dat_str0.replace('\n','No')
                                str_cond.append(dat_str0)
                            
                            dat_str += dat_str0
                            dat_str += ','
                        
                        requestIns = ""
                        requestIns += 'UPDATE "'
                        requestIns += head_table
                        requestIns += '" set sogl ='
                        requestIns += "'"+str(str_cond[2])+"'"
                        requestIns += " WHERE id ="
                        requestIns += "'"+str(str_cond[0])+"'"
                        UGNTU_DB.Exe

        UGNTU_DB.CLOSE

class Filter:
    def __init__(self):
        return 0
    def main(self):
        BGU_DB.Connect
        UGATU_DB.Connect
        UGNTU_DB.Connect

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

        tablesUgntu = ['Списки поступающих: БАГ БАГ Автоматизация технологических процессов и производств (в нефтяной и газовой промышленности) (г. Уфа)',
        'Списки поступающих: БАТ БАТ Автоматизация технологических процессов и производств (в нефтепереработке и нефтехимии) (г. Уфа)',
        'Списки поступающих: БИФ БИФ Прикладная информатика в экономике и финансах ТЭК (г. Уфа)',
        'Списки поступающих: БПО БПО Программное обеспечение средств вычислительной техники и автоматизированных систем (г. Уфа)']



        #те, кто подал заявление в бгу, удаляются из угату
        #------------------#

        
        for k in tablesBGU: 
            requestBGU = ""
            requestBGU +='select id from "'  
            requestBGU += k
            requestBGU +='" where sogl  = 1'
            BGU_DB.ExeBGU
            
            for row in BGU_DB.ExeBGU:  
                
                for i in tablesUgatu:
                    #requestString3 = ("delete from ", i,"where id =",row)
                    requestUgatu = ""
                    requestUgatu += 'delete from "'
                    requestUgatu += str(i)
                    requestUgatu += '" where id = '
                    requestUgatu += "'"
                    requestUgatu += row[0]
                    requestUgatu += "'"
                    UGATU_DB.ExeUGATU
                    

        #-----------------#



        #удаляем тех, кто подал согласие в Угату, из БГУ
        #\\\\\\\\\\\\\\\\\#

        for k in tablesUgatu: 
            requestUgatu = ""
            requestUgatu +='select id from "'  
            requestUgatu += k
            requestUgatu +='" where sogl  = '
            requestUgatu += "'Yes'"
            UGATU_DB.ExeUGATU
            
            for row in UGATU_DB.ExeUGATU:  
                
                for i in tablesBGU:
                    #requestString3 = ("delete from ", i,"where id =",row)
                    requestBGU = ""
                    requestBGU += 'delete from "'
                    requestBGU += str(i)
                    requestBGU += '" where id = '
                    requestBGU += "'"
                    requestBGU += row[0]
                    requestBGU += "'"
                    UGATU_DB.ExeUGATU
                    
        #\\\\\\\\\\\\\\\\\#







        #удаляем тех, кто уже подал заявление, с других специальностей Угату
        #===================#

        for s in tablesUgatu:
            requestUgatu = ""
            requestUgatu +='select id from "'  
            requestUgatu += s
            requestUgatu +='" where sogl  = '
            requestUgatu += "'Yes'"
            UGATU_DB.ExeUGATU

        
        
            for row in UGATU_DB.ExeUGATU:
                
                for m in tablesUgatu:
                    requestUgatu_1 = ""
                    requestUgatu_1 += 'delete from "'
                    requestUgatu_1 += m
                    requestUgatu_1 += '" where id = '
                    requestUgatu_1 += "'"
                    requestUgatu_1 += row[0]
                    requestUgatu_1 += "'"
                    requestUgatu_1 += ' and sogl =  '
                    requestUgatu_1 +=  "'No'"
                    UGATU_DB.Exe_1
                    

            
            #=====================#





        #Удаляем из списков угату всех, кто "На другом специальности"
        #+++++++++++++++++++#

        for i in tablesUgatu:
            requestUgatu = ""
            requestUgatu +='delete from "' 
            requestUgatu += i
            requestUgatu +='" where sogl  = '
            requestUgatu += "'On another specialty'"
            UGATU_DB.ExeUGATU

            

        #+++++++++++++++++++#










        #те, кто подал заявление в бгу на одном направлении, удаляются из других
        #~~~~~~~~~~~~~~~~~#


        for s in tablesBGU:
            requestBGU = ""
            requestBGU +='select id from "'  
            requestBGU += s
            requestBGU +='" where sogl  = 1'
            BGU_DB.ExeBGU

            
            for row in BGU_DB.ExeBGU:
                
                for m in tablesBGU:
                    requestBGU_1 = ""
                    requestBGU_1 += 'delete from "'
                    requestBGU_1 += m
                    requestBGU_1 += '" where id = '
                    requestBGU_1 += "'"
                    requestBGU_1 += row[0]
                    requestBGU_1 += "'"
                    requestBGU_1 += ' and sogl = 0'
                    BGU_DB.Exe_1
                    
            

        #~~~~~~~~~~~~~~~~~~#



        #Удалить всех из Угату и Бгу, кто подал заявление в УГНТУ#

        

        

        for s in tablesUgntu:
            requestUgntu = ""
            requestUgntu +='select id from "'  
            requestUgntu += s
            requestUgntu +='" where sogl  = '
            requestUgntu += "'Yes'"
            UGNTU_DB.ExeUGNTU
            
            for row in UGNTU_DB.ExeUGNTU:
                
                for m in tablesBGU:
                    requestBGU_1 = ""
                    requestBGU_1 += 'delete from "'
                    requestBGU_1 += m
                    requestBGU_1 += '" where id = '
                    requestBGU_1 += "'"
                    requestBGU_1 += row[0]
                    requestBGU_1 += "'"
                    requestBGU_1 += ' and sogl = 0'
                    BGU_DB.Exe_1
                    
                for m in tablesUgatu:
                    requestUgatu_1 = ""
                    requestUgatu_1 += 'delete from "'
                    requestUgatu_1 += m
                    requestUgatu_1 += '" where id = '
                    requestUgatu_1 += "'"
                    requestUgatu_1 += row[0]
                    requestUgatu_1 += "'"
                    requestUgatu_1 += ' and sogl =  '
                    requestUgatu_1 +=  "'No'"
                    UGATU_DB.Exe_1
                    


        UGATU_DB.CLOSE

        UGNTU_DB.CLOSE

        BGU_DB.CLOSE


UGATU.main
BGU.main
UGNTU.main
Filter.main

