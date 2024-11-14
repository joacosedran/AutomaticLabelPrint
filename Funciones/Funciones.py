import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')

import pandas as pd
import typer

from InquirerPy import inquirer
from rich import print

from Impresora import imprimir_etiqueta

from Clases.Clase_Administracion import Administracion
from Clases.Clase_Electronica import Electronica
from Clases.Clase_Gerencia import Gerencia
from Clases.Clase_Ingenieria import Ingenieria
from Clases.Clase_Panol import Panol
from Clases.Clase_Produccion import Produccion
from Clases.Clase_Sistemas import Sistemas
from Clases.Clase_Tesoreria import Tesoreria
from Clases.Clase_Ventas import Ventas

#---------------------------------------------------------------------GENERICAS---------------------------------------------------------------------#

def cargar_datos(clase_equipo):
    df = pd.read_excel(clase_equipo.RUTA, sheet_name=clase_equipo.HOJA)
    equipos = []
    print(f"Datos cargados desde el Excel: {clase_equipo.RUTA} - {clase_equipo.HOJA}")    
    for _, row in df.iterrows():
        equipo = clase_equipo(row['ID'],
                              row['Tipo'],
                              row['SO'],
                              row['Marca'],
                              row['Usuarios'],
                              row['Antiguedad'],
                              row['Gama'],
                              row['Disco'],
                              row['Estado'],
                              row['Modelo']
                              )
        equipos.append(equipo)    
    return equipos

def obtener_opciones_departamento():
    return [
        {"name": "Administración", "value": Administracion},
        {"name": "Electrónica", "value": Electronica},
        {"name": "Gerencia", "value": Gerencia},
        {"name": "Ingeniería", "value": Ingenieria},
        {"name": "Pañol", "value": Panol},
        {"name": "Producción", "value": Produccion},
        {"name": "Sistemas", "value": Sistemas},
        {"name": "Tesorería", "value": Tesoreria},
        {"name": "Ventas", "value": Ventas}
    ]

def seleccionar_departamento(message="Selecciona un departamento:"):
    opciones = obtener_opciones_departamento()
    departamento_seleccionado = inquirer.select(
        message=message,
        choices=opciones,
        pointer="♦️ ",
    ).execute()
    return departamento_seleccionado

#---------------------------------------------------------------------MENU---------------------------------------------------------------------#

def menu_opciones():
    opciones = [
        {"name": "1 Imprimir todas las etiquetas", "value": "todas"},
        {"name": "2 Imprimir todas las etiquetas de un Departamento", "value": "seleccionarDepartamento"},
        {"name": "3 Imprimir una sola etiqueta", "value": "imprimirEtiqueta"},
        {"name": "4 Imprimir el último registro", "value": "ultimoRegistro"},
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
        seleccionar_departamento_para_imprimir()
    elif opcion_seleccionada == "imprimirEtiqueta":
        seleccionar_departamento_para_un_equipo()
    elif opcion_seleccionada == "ultimoRegistro":
        seleccionar_departamento_para_ultimo_registro()
    elif opcion_seleccionada == "salir":
        print("[magenta]Gracias por usar el programa[/magenta]. ¡Hasta luego!")
        raise typer.Exit()

#---------------------------------------------------------------------SELECCION---------------------------------------------------------------------#

def seleccionar_departamento_para_ultimo_registro():
    departamento_seleccionado = seleccionar_departamento("Selecciona un departamento para el último registro:")
    equipos_vector = cargar_datos(departamento_seleccionado)
    
    if equipos_vector:
        ultimo_equipo = max(equipos_vector, key=lambda e: e.equip_id)
        imprimir_equipos(ultimo_equipo)
    else:
        print("No hay equipos en el departamento seleccionado.")
    menu_opciones()

def seleccionar_departamento_para_imprimir():
    departamento_seleccionado = seleccionar_departamento("Selecciona un departamento:")
    equipos_vector = cargar_datos(departamento_seleccionado)

    if not equipos_vector:
        print("No se encontraron equipos en este departamento.")
        return
    
    tipos_dispositivos = set(e.tipo for e in equipos_vector)
    opciones = [{"name": tipo, "value": tipo} for tipo in tipos_dispositivos]
    
    tipo_seleccionado = inquirer.select(
        message="Selecciona el tipo de dispositivo:",
        choices=opciones,
        pointer="♦️ ",
    ).execute()

    equipos_filtrados = [e for e in equipos_vector if e.tipo == tipo_seleccionado]
    
    if equipos_filtrados:
        imprimir_equipos(equipos_filtrados)
    else:
        print(f"No hay equipos de tipo '{tipo_seleccionado}' en este departamento.")


def seleccionar_departamento_para_un_equipo():
    departamento_seleccionado = seleccionar_departamento("Selecciona un departamento:")
    equipos_vector = cargar_datos(departamento_seleccionado)
    if any(isinstance(e, list) for e in equipos_vector):
        print("¡Error! Se ha creado una lista de listas al filtrar equipos.")
        print("Equipos filtrados:", equipos_vector)
        return
    imprimir_un_equipo(equipos_vector)

#---------------------------------------------------------------------IMPRESION---------------------------------------------------------------------#

def imprimir_todas_las_etiquetas():
    equipos_vector = []
    for departamento in obtener_opciones_departamento():
        equipos_vector += cargar_datos(departamento["value"])
    imprimir_etiqueta(equipos_vector)
    menu_opciones()

def imprimir_un_equipo(equipos_vector):
    print("IDs disponibles:", [e.equip_id for e in equipos_vector])
    while True:
        equip_id = input("Ingrese el ID del equipo a imprimir: ")
        equipo_encontrado = next((e for e in equipos_vector if str(e.equip_id) == str(equip_id)), None)
        if equipo_encontrado:
            imprimir_etiqueta([equipo_encontrado])
            break
        else:
            print("ID no encontrada, ingrese nuevamente:") 
    menu_opciones()

def imprimir_equipos(equipos_vector):
    if not equipos_vector:
        print("No hay equipos para mostrar.")
    else:
        imprimir_etiqueta(equipos_vector)
    menu_opciones()
        
#---------------------------------------------------------------------EJECUCION---------------------------------------------------------------------#

def main():
    menu_opciones()

if __name__ == "__main__":
    typer.run(main)