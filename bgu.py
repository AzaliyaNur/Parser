from os import lstat
from bs4 import BeautifulSoup
import requests
import csv

url = 'https://pk-inf.bashedu.ru/static/file_vault/БашГУ 11.03.02_ФТИ_Инфокоммуникационные технологии и системы связи_О_Б.HTML'
html = requests.get(url)
print(html)
soup = BeautifulSoup(html.text, 'html.parser')
file = open('abiturients.csv',encoding='utf-8', mode = "w")



#for supchik in soup.find_all('table'):
for supik in soup.find_all('tr', class_='R0'):
    if supik.find('td', class_ = 'R12C0') is not None:
        csv_str = ""
        for sup in supik.find_all('td', class_='R12C0'):
            
            sup_txt = sup.text
            #if sup_txt == ' ':
                #sup_txt = sup_txt.replace('','0')
            csv_str += sup_txt.replace('\n', '')
            csv_str += ';'
        csv_str += '\n'
        print(csv_str)
        file.write(csv_str)
file.close()
