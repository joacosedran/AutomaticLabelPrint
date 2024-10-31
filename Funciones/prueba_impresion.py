import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')

import pandas as pd
import typer

from tabulate import tabulate
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

#---------------------------------------------------------------------DATOS---------------------------------------------------------------------#


def cargar_datos(clase_equipo):
    df = pd.read_excel(clase_equipo.RUTA, sheet_name=clase_equipo.HOJA)
    equipos = []
    
    print(f"Datos cargados desde el Excel: {clase_equipo.RUTA} - {clase_equipo.HOJA}")    
    for _, row in df.iterrows():
        equipo = clase_equipo(row['ID'], row['Tipo'], row['Modelo'], row['SO'],
                              row['Marca'], row['Usuarios'], row['Antiguedad'],
                              row['Gama'], row['Disco'], row['Costo (U$D)'],
                              row['Estado'],
                              )
        equipos.append(equipo)
        
    return equipos


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
        seleccionar_departamento()
    elif opcion_seleccionada == "imprimirEtiqueta":
        seleccionar_departamento_para_un_equipo()
    elif opcion_seleccionada == "ultimoRegistro":
        seleccionar_departamento_para_ultimo_registro()
    elif opcion_seleccionada == "salir":
        print("[magenta]Gracias por usar el programa[/magenta]. ¡Hasta luego!")
        raise typer.Exit()


def volver_menu():
    opcion_seleccionada = inquirer.select(
        message="¿Quieres regresar al menú principal?",
        choices=["Y", "N"]
    ).execute()
    if opcion_seleccionada == "Y":
        menu_opciones()
    else:
        print("[magenta]Gracias por usar el programa[/magenta]. ¡Hasta luego!")

#---------------------------------------------------------------------SELECCION---------------------------------------------------------------------#

def seleccionar_departamento_para_ultimo_registro():
    opciones = [
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
    departamento_seleccionado = inquirer.select(
        message="Selecciona un departamento:",
        choices=opciones,
        pointer="♦️ ",
    ).execute()
    equipos_vector = cargar_datos(departamento_seleccionado)
    
    # Encuentra el equipo con el mayor ID
    if equipos_vector:
        ultimo_equipo = max(equipos_vector, key=lambda e: e.equip_id)
        print([ultimo_equipo])
    else:
        print("No hay equipos en el departamento seleccionado.")


def seleccionar_departamento():
    opciones = [
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
    departamento_seleccionado = inquirer.select(
        message="Selecciona un departamento:",
        choices=opciones,
        pointer="♦️ ",
    ).execute()
    equipos_vector = cargar_datos(departamento_seleccionado)
    seleccionar_tipo_de_equipo(equipos_vector)


def seleccionar_tipo_de_equipo(equipos_vector):
    tipos_dispositivos = set(e.tipo for e in equipos_vector)
    opciones = [{"name": tipo, "value": tipo} for tipo in tipos_dispositivos]
    
    tipo_seleccionado = inquirer.select(
        message="Selecciona el tipo de dispositivo:",
        choices=opciones,
        pointer="♦️ ",
    ).execute()
    equipos_filtrados = [e for e in equipos_vector if e.tipo == tipo_seleccionado]
    imprimir_todos_los_equipos(equipos_filtrados)


def seleccionar_departamento_para_un_equipo():
    opciones = [
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
    departamento_seleccionado = inquirer.select(
        message="Selecciona un departamento:",
        choices=opciones,
        pointer="♦️ ",
    ).execute()
    equipos_vector = cargar_datos(departamento_seleccionado)
    if departamento_seleccionado == Administracion:
        departamento = "Administración"
    imprimir_un_equipo(equipos_vector, departamento_seleccionado)

#---------------------------------------------------------------------IMPRESION---------------------------------------------------------------------#

def imprimir_todas_las_etiquetas():
    equipos_administracion = cargar_datos(Administracion)
    equipos_electronica = cargar_datos(Electronica)
    equipos_gerencia = cargar_datos(Gerencia)
    equipos_ingenieria = cargar_datos(Ingenieria)
    equipos_panol = cargar_datos(Panol)
    equipos_produccion = cargar_datos(Produccion)
    equipos_sistemas = cargar_datos(Sistemas)
    equipos_tesoreria = cargar_datos(Tesoreria)
    equipos_ventas = cargar_datos(Ventas)
    equipos_vector = equipos_administracion + equipos_electronica + equipos_gerencia + equipos_ingenieria + equipos_panol + equipos_produccion + equipos_sistemas + equipos_tesoreria + equipos_ventas
    imprimir_todos_los_equipos(equipos_vector)


def imprimir_todos_los_equipos(equipos_vector):
    if not equipos_vector:
        print("No hay equipos para mostrar.")
    else:
        # Convertir la lista de objetos a una lista de listas para tabulate
        equipos_tabla = [[e.equip_id, e.tipo, e.modelo, e.os, e.marca, e.usuarios, e.antiguedad, e.gama, e.disco, e.cto_adq_usd, e.estado] for e in equipos_vector]
        imprimir_etiqueta(equipos_tabla)
    volver_menu()


def imprimir_un_equipo(equipos_vector, departamento):
    print("IDs disponibles:", [e.equip_id 
                               for e in equipos_vector])
    while True:
        equip_id = input("Ingrese el ID del equipo a imprimir: ")
        equipo_encontrado = next((e for e in equipos_vector if str(e.equip_id) == str(equip_id)), None)
        if equipo_encontrado:
            equipos_tabla = [
                equipo_encontrado.equip_id, equipo_encontrado.tipo, equipo_encontrado.os, 
                equipo_encontrado.marca, equipo_encontrado.usuarios, equipo_encontrado.antiguedad, 
                equipo_encontrado.gama, equipo_encontrado.disco, equipo_encontrado.cto_adq_usd, 
                equipo_encontrado.estado, equipo_encontrado.modelo
            ]
            imprimir_etiqueta(equipos_tabla, departamento)
            break
        else:
            print("ID no encontrada, ingrese nuevamente:")
    menu_opciones()

#---------------------------------------------------------------------EJECUCION---------------------------------------------------------------------#

def main():
    menu_opciones()
    
if __name__ == "__main__":
    typer.run(main)
