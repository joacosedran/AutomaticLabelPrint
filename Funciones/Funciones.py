import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')

import pandas as pd
import typer

from tabulate import tabulate
from InquirerPy import inquirer
from rich import print

from Clases.Clase_Administracion import Administracion
from Clases.Clase_Ingenieria import Ingenieria
from Clases.Clase_Produccion import Produccion

def cargar_datos(clase_equipo):
    df = pd.read_excel(clase_equipo.RUTA, sheet_name=clase_equipo.HOJA)
    equipos = []
    
    print(f"Datos cargados desde el Excel: {clase_equipo.RUTA} - {clase_equipo.HOJA}")    
    for _, row in df.iterrows():
        equipo = clase_equipo(row['ID'], row['TIPO'], row['OS'], row['MARCA'],
                              row['USUARIOS'], row['ANTIGUEDAD'], row['GAMA'],
                              row['DISCO'], row['CtoAdq_USD'], row['ESTADO'],
                              row['MODELO'])
        equipos.append(equipo)
        
    return equipos

def menu_opciones():
    opciones = [
        {"name": "1 Imprimir todas las etiquetas", "value": "todas"},
        {"name": "2 Imprimir todas las etiquetas de un Departamento", "value": "seleccionarDepartamento"},
        {"name": "3 Imprimir una sola etiqueta", "value": "imprimirEtiqueta"},
        {"name": "Salir", "value": "salir"}
    ]
    opcion_seleccionada = inquirer.select(
        message="Selecciona una opción:",
        choices=opciones,
        pointer="♦️ ",
    ).execute()
    if opcion_seleccionada == "todas":
        imprimir_todas_las_etiquetas()
    elif opcion_seleccionada == "seleccionarDepartamento":
        seleccionar_departamento()
    elif opcion_seleccionada == "imprimirEtiqueta":
        seleccionar_departamento_para_un_equipo()
    elif opcion_seleccionada == "salir":
        print("[magenta]Gracias por usar el programa[/magenta]. ¡Hasta luego!")
        raise typer.Exit()

def seleccionar_departamento_para_un_equipo():
    opciones = [
        {"name": "Ingeniería", "value": Ingenieria},
        {"name": "Producción", "value": Produccion}
    ]
    departamento_seleccionado = inquirer.select(
        message="Selecciona un departamento:",
        choices=opciones,
        pointer="♦️ ",
    ).execute()
    equipos_vector = cargar_datos(departamento_seleccionado)
    imprimir_un_equipo(equipos_vector)

def imprimir_todas_las_etiquetas():
    equipos_ingenieria = cargar_datos(Ingenieria)
    equipos_produccion = cargar_datos(Produccion)
    equipos_vector = equipos_ingenieria + equipos_produccion
    imprimir_todos_los_equipos(equipos_vector)

def seleccionar_departamento():
    opciones = [
        {"name": "Ingeniería", "value": Ingenieria},
        {"name": "Producción", "value": Produccion},
        {"name": "Administracion", "value": Administracion}
    ]
    departamento_seleccionado = inquirer.select(
        message="Selecciona un departamento:",
        choices=opciones,
        pointer="♦️ ",
    ).execute()
    equipos_vector = cargar_datos(departamento_seleccionado)
    imprimir_todos_los_equipos(equipos_vector)

def imprimir_todos_los_equipos(equipos_vector):
    if not equipos_vector:
        print("No hay equipos para mostrar.")
    else:
        # Convertir la lista de objetos a una lista de listas para tabulate
        equipos_tabla = [[e.equip_id, e.tipo, e.os, e.marca, e.usuarios, e.antiguedad, e.gama, e.disco, e.cto_adq_usd, e.estado, e.modelo] for e in equipos_vector]
        headers = ["ID", "TIPO", "OS", "MARCA", "USUARIOS", "ANTIGÜEDAD", "GAMA", "DISCO", "CtoAdq_USD", "ESTADO", "MODELO"]
        
        tabla = tabulate(equipos_tabla, headers=headers, tablefmt="fancy_grid")
        print(tabla)
    volver_menu()

def imprimir_un_equipo(equipos_vector):
    print("IDs disponibles:", [e.equip_id for e in equipos_vector])
    while True:
        equip_id = input("Ingrese el ID del equipo a imprimir: ")
        equipo_encontrado = next((e for e in equipos_vector if str(e.equip_id) == str(equip_id)), None)
        if equipo_encontrado:
            equipo_tabla = [[
                equipo_encontrado.equip_id, equipo_encontrado.tipo, equipo_encontrado.os, 
                equipo_encontrado.marca, equipo_encontrado.usuarios, equipo_encontrado.antiguedad, 
                equipo_encontrado.gama, equipo_encontrado.disco, equipo_encontrado.cto_adq_usd, 
                equipo_encontrado.estado, equipo_encontrado.modelo
            ]]
            headers = ["ID", "TIPO", "OS", "MARCA", "USUARIOS", "ANTIGÜEDAD", "GAMA", "DISCO", "CtoAdq_USD", "ESTADO", "MODELO"]
            tabla = tabulate(equipo_tabla, headers=headers, tablefmt="fancy_grid")
            print(tabla)
            break
        else:
            print("ID no encontrada, ingrese nuevamente:")
    volver_menu()

def volver_menu():
    opcion_seleccionada = inquirer.select(
        message="¿Quieres regresar al menú principal?",
        choices=["Y", "N"]
    ).execute()
    if opcion_seleccionada == "Y":
        menu_opciones()
    else:
        print("[magenta]Gracias por usar el programa[/magenta]. ¡Hasta luego!")

def main():
    menu_opciones()
    
if __name__ == "__main__":
    typer.run(main)