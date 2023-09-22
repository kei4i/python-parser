#-*- coding: utf-8 -*-
import	requests
import csv
from bs4 import BeautifulSoup, Tag
link = "https://icanhazip.com"
vocubulary = []

verbs = ['sentir','calentar','empezar','despertar','mentir','perder','entendés','contar','costar','dormir','encontrar','volver','soñar','recordar','medir','reír','despedir','impedir','vestir','repetir','servir','elegir','seguir','jugar','traducir','salir','saber','dar','ver','estar','caber','huir','construir','sustituir','incluir','atribuir','traer','hacer','poner','conocer','conducir','parecer','ir']

for i, verb in enumerate(verbs):    
    link2 = f"https://www.wordreference.com/conj/esverbs.aspx?v={verb}"
    response = requests.get(link2).text
    soup = BeautifulSoup(response, 'lxml')
    block = soup.find('table', id = "contenttable")
    allTables = block.find_all('table', class_ = "neoConj")
    indicativoPresente = allTables[0]
    imperativoAlfirmativo = allTables[15]
    imperativoNegativo = allTables[16]
    columnSecond = ''
    for tr in imperativoAlfirmativo:
        firstColumn = tr.find('th')
        secondColumn = tr.find('td')
        if type(firstColumn) == Tag and type(secondColumn) == Tag:
            secondColumnText = secondColumn.text.strip()
            if secondColumnText != "-" and secondColumnText != "–":
                columnSecond+="<div>" + firstColumn.text + " {{c1::" + secondColumn.text + "}}</div>"
    vocubulary.append([verb, f"{columnSecond}"])

with open('imperativoAlfirmativo.csv', 'w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL, delimiter=';')
    writer.writerows(vocubulary)