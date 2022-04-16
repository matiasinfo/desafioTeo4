from collections import Counter
import csv
import os
from re import A
from consolemenu import ConsoleMenu
from consolemenu.items import *

base_path = os.path.abspath(os.path.dirname(__file__))
archivo_netflix = f'{base_path}\\netflix_titles.csv'

archivo =  open("netflix_titles.csv",encoding="UTF-8")
csvreader = csv.reader(archivo, delimiter= ",")
encabezado = next(csvreader)
pelis2021 = list(filter(lambda elem: elem[1] == "Movie" and elem[7] == "2021", csvreader ))
archivo.close()
print(archivo_netflix," esta es la url que mandamos como nombre de archivo")
print(len(pelis2021))

def peliculas_2021(pelis2021):
    with open("pelis2021.csv","w",encoding="UTF-8") as writer_csv:
        writer = csv.writer(writer_csv)
        for elem in pelis2021:
            writer.writerow(elem)
    

def paises_mas_producciones(pelis2021):
    paises = []
    for elem in pelis2021:
        if not elem[5]== " ":
            if not elem[5]== "":
                paises.append(elem[5]) 
    contador = Counter(paises)
    print(contador.most_common(5)) 


texto1 = "Menu desafio"
texto2 = " punto 1 y punto 2"
menu = ConsoleMenu(texto1, texto2)
function_item1 = FunctionItem("Mostrar pelis", peliculas_2021, [pelis2021])
function_item2 = FunctionItem("Paises con mas producciones", paises_mas_producciones, [pelis2021])
menu.append_item(function_item1)
menu.append_item(function_item2)
menu.show()