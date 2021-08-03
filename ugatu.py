from os import lstat
from bs4 import BeautifulSoup
import requests
import csv
import pyodbc


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
'141',
'142',
'143',
'144',
'145',
'146',
'147',
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
#for k in range (1,33):
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

    #парсим
    arr = []
    arr_num = 0
    file = open(head_csv + ".csv", "w")

    for t_data in soup.find_all('table'):
        lt = []
        for tb_data in t_data.find_all('tbody'):
            for data in tb_data.find_all('tr'): #Находим все данные из таблицы
                csv_str = ""
                csv_str += data.find_all('td')[2].text
                csv_str += ";"
                csv_str += data.find_all('td')[3].text
                csv_str += ";"
                csv_str += data.find_all('td')[4].text
                csv_str += ";"
                csv_str += data.find_all('td')[5].text
                csv_str += ";"
                csv_str += data.find_all('td')[6].text
                csv_str += ";"
                csv_str += data.find_all('td')[7].text
                csv_str += ";"
                csv_str += data.find_all('td')[8].text
                csv_str += ";\n"
                # 
                lt.append(csv_str)
        arr.append(lt)
        arr_num = arr_num + 1
                #print(csv_str)
    if arr_num > 0:
        for str in arr[arr_num-1]:
            file.write(str)   

    file.close()


    


      
    



    



 









