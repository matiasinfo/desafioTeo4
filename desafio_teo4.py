from collections import Counter
import csv
import os
from consolemenu import ConsoleMenu
from consolemenu.items import *

def abrir_archivo():
    """ abrimos el arhivo de titulos de netflix para trabajar con su informacion
        a travez de un filtrado de las peliculas del año 2021 """
    base_path = os.path.abspath(os.path.dirname(__file__))
    archivo_netflix = f'{base_path}\\netflix_titles.csv'
    archivo =  open("netflix_titles.csv",encoding="UTF-8")
    csvreader = csv.reader(archivo, delimiter= ",")
    encabezado = next(csvreader)
    pelis2021 = list(filter(lambda elem: elem[1] == "Movie" and elem[7] == "2021", csvreader ))
    archivo.close()
    return pelis2021


def peliculas_2021(pelis2021):
    """ generamos un nuevo archivo csv para las peliculas del 2021"""
    with open("pelis2021.csv","w",encoding="UTF-8") as writer_csv:
        writer = csv.writer(writer_csv)
        for elem in pelis2021:
            writer.writerow(elem)
    

def paises_mas_producciones(pelis2021):
    """ creamos una nueva lista de paises ,
        usamos la clase Counter para obtener los 5 con mas producciones  """
    caracteres = (""," ",",",".")
    paises = [elem[5] for elem in pelis2021 if not elem[5] in caracteres]
    contador = Counter(paises)
    print(contador.most_common(5)) 

def creamos_menu(pelis2021):
    """ utilizando el modulo console-menu generamos un menu "interactivo " 
        que nos brinda las 3 acciones disponibles """
    texto1 = "Menu desafio"
    texto2 = " punto 1 y punto 2"
    menu = ConsoleMenu(texto1, texto2)
    function_item1 = FunctionItem("crear archivo de peliculas 2021", peliculas_2021, [pelis2021])
    function_item2 = FunctionItem("Paises con mas producciones", paises_mas_producciones, [pelis2021])
    menu.append_item(function_item1)
    menu.append_item(function_item2)
    return menu


def main():
    pelis2021 = abrir_archivo()
    #paises_mas_producciones(pelis2021)
    menu = creamos_menu(pelis2021)  #estoy teniendo problemas con la visualizacion del punto2
    menu.show()

if __name__ == '__main__':
    main()