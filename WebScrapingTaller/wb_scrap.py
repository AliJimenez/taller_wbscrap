import requests
import pandas as pd
from bs4 import BeautifulSoup

Fecha = []
PIB_anual = []
Var_PIB = []

url = 'https://datosmacro.expansion.com/pib/ecuador'

# obtengo la pagina a analizar
html_doc = requests.get(url)
soup = BeautifulSoup(html_doc.text, 'html.parser')

tabla = soup.find('table', attrs={'class':'table tabledat table-striped table-condensed table-hover'})
print(tabla)

fecha_list = tabla.find_all(attrs={'class': 'fecha'})
pib_anual_list = tabla.find_all(attrs={'class':'numero eur'})
var_pib_list = tabla.find_all(attrs={'class':'numero dol'})


for fecha in fecha_list:
    print(fecha.text)
    Fecha.append(fecha.text)
for pib_anual in pib_anual_list:
    print(pib_anual.text)
    PIB_anual.append(pib_anual.text)
for var_pib in var_pib_list:
    print(var_pib.text)
    Var_PIB.append(var_pib.text)



df = pd.DataFrame({'Fecha':Fecha, 'Producto Interno Bruto Anual':PIB_anual, 'Var PIB (%)':Var_PIB})
df.to_csv('pib.csv', index=False, encoding='utf-8')
