import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:8000/'

html_doc = requests.get(url)

soup = BeautifulSoup(html_doc.text, 'html.parser')

titulo_datos = soup.h1.string
print(titulo_datos)

tabla = soup.find('table')

filas = tabla.find_all('tr')

nombres = []
apellidos = []
emails = []
departamentos = []

for fila in filas:

    celdas = fila.find_all('td')
    if len(celdas)>0:
        print(celdas[1].string)
        nombres.append(celdas[1].string)
        print(celdas[2].string)
        apellidos.append(celdas[2].string)
        print(celdas[4].string)
        emails.append(celdas[4].string)
        print(celdas[7].string)
        departamentos.append(celdas[7].string)
print(nombres)
print(apellidos)
print(emails)
print(departamentos)

df = pd.DataFrame({'Nombres': nombres, 'Apellidos': apellidos, 'Emails': emails, 'Departamentos': departamentos})
df.to_csv('empleados.csv', index=False, encoding='UTF-8')
