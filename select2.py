import pyodbc 
from datetime import datetime

#connect to server

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



#те, кто подал заявление в бгу, удаляются из угату
#------------------#

 
for k in tablesBGU: 
    requestBGU = ""
    requestBGU +='select id from "'  
    requestBGU += k
    requestBGU +='" where sogl  = 1'
    cursorBGU.execute(requestBGU)
    
    for row in cursorBGU:  
        
        for i in tablesUgatu:
            #requestString3 = ("delete from ", i,"where id =",row)
            requestUgatu = ""
            requestUgatu += 'delete from "'
            requestUgatu += str(i)
            requestUgatu += '" where id = '
            requestUgatu += "'"
            requestUgatu += row[0]
            requestUgatu += "'"
            cursorUGATU.execute(requestUgatu)
            

#-----------------#



#удаляем тех, кто подал согласие в Угату, из БГУ
#\\\\\\\\\\\\\\\\\#

for k in tablesUgatu: 
    requestUgatu = ""
    requestUgatu +='select id from "'  
    requestUgatu += k
    requestUgatu +='" where sogl  = '
    requestUgatu += "'Yes'"
    cursorUGATU.execute(requestUgatu)
    
    for row in cursorUGATU:  
        
        for i in tablesBGU:
            #requestString3 = ("delete from ", i,"where id =",row)
            requestBGU = ""
            requestBGU += 'delete from "'
            requestBGU += str(i)
            requestBGU += '" where id = '
            requestBGU += "'"
            requestBGU += row[0]
            requestBGU += "'"
            cursorBGU.execute(requestBGU)
            
#\\\\\\\\\\\\\\\\\#







#удаляем тех, кто уже подал заявление, с других специальностей Угату
#===================#

for s in tablesUgatu:
    requestUgatu = ""
    requestUgatu +='select id from "'  
    requestUgatu += s
    requestUgatu +='" where sogl  = '
    requestUgatu += "'Yes'"
    cursorUGATU.execute(requestUgatu)

   
   
    for row in cursorUGATU.fetchall():
        
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
            cursorUGATU.execute(requestUgatu_1)
            

    
    #=====================#





#Удаляем из списков угату всех, кто "На другом специальности"
#+++++++++++++++++++#

for i in tablesUgatu:
    requestUgatu = ""
    requestUgatu +='delete from "' 
    requestUgatu += i
    requestUgatu +='" where sogl  = '
    requestUgatu += "'On another specialty'"
    cursorUGATU.execute(requestUgatu)

    

#+++++++++++++++++++#










#те, кто подал заявление в бгу на одном направлении, удаляются из других
#~~~~~~~~~~~~~~~~~#


for s in tablesBGU:
    requestBGU = ""
    requestBGU +='select id from "'  
    requestBGU += s
    requestBGU +='" where sogl  = 1'
    cursorBGU.execute(requestBGU)

    
    for row in cursorBGU.fetchall():
        
        for m in tablesBGU:
            requestBGU_1 = ""
            requestBGU_1 += 'delete from "'
            requestBGU_1 += m
            requestBGU_1 += '" where id = '
            requestBGU_1 += "'"
            requestBGU_1 += row[0]
            requestBGU_1 += "'"
            requestBGU_1 += ' and sogl = 0'
            cursorBGU.execute(requestBGU_1)
            
    

#~~~~~~~~~~~~~~~~~~#



#Удалить всех из Угату и Бгу, кто подал заявление в УГНТУ#

tablesUgntu = ['Списки поступающих: БАГ БАГ Автоматизация технологических процессов и производств (в нефтяной и газовой промышленности) (г. Уфа)',
'Списки поступающих: БАТ БАТ Автоматизация технологических процессов и производств (в нефтепереработке и нефтехимии) (г. Уфа)',
'Списки поступающих: БИФ БИФ Прикладная информатика в экономике и финансах ТЭК (г. Уфа)',
'Списки поступающих: БПО БПО Программное обеспечение средств вычислительной техники и автоматизированных систем (г. Уфа)']

cnxnUGNTU = pyodbc.connect("Driver={SQL Server Native Client 10.0};"
                                    "Server=WIN-K1RC9U9RIIK\SQLS;"
                                    "Database=UGNTU;"
                                    "Trusted_Connection=yes;")
cursorUGNTU = cnxnUGNTU.cursor()

for s in tablesUgntu:
    requestUgntu = ""
    requestUgntu +='select id from "'  
    requestUgntu += s
    requestUgntu +='" where sogl  = '
    requestUgntu += "'Yes'"
    cursorUGNTU.execute(requestUgntu)
    
    for row in cursorUGNTU.fetchall():
        
        for m in tablesBGU:
            requestBGU_1 = ""
            requestBGU_1 += 'delete from "'
            requestBGU_1 += m
            requestBGU_1 += '" where id = '
            requestBGU_1 += "'"
            requestBGU_1 += row[0]
            requestBGU_1 += "'"
            requestBGU_1 += ' and sogl = 0'
            cursorBGU.execute(requestBGU_1)
            
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
            cursorUGATU.execute(requestUgatu_1)
            


cnxnUGNTU.commit()
cnxnUGNTU.close()

cnxnBGU.commit()
cnxnBGU.close()

cnxnUGATU.commit()
cnxnUGATU.close()
