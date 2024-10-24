#class_gestion.py

import pandas as pd
from class_equipos import Equipos

class GestorEquipos:
    """
    Manages a collection of equipment items loaded from an Excel file.

    This class provides methods to load equipment data, display details 
    of individual equipment items, and print the information of all equipment.
    """

    def __init__(self, ruta_inge, sheet_inge):
        """Initialize the GestorEquipos with the path to the Excel file and sheet name."""
        self.equipos_vector = self.cargar_datos(ruta_inge, sheet_inge)

    def cargar_datos(self, ruta_inge, sheet_inge):
        """Load equipment data from an Excel file into a list of Equipos objects."""
        df = pd.read_excel(ruta_inge, sheet_name=sheet_inge)
        equipos = []
        
        # Mostrar los datos del DataFrame para depuración
        print("Datos cargados desde el Excel:")
        print(df)

        for _, row in df.iterrows():
            equipo = Equipos(row['ID'], row['TIPO'], row['OS'], row['MARCA'], 
                            row['USUARIOS'], row['ANTIGUEDAD'], row['GAMA'], 
                            row['DISCO'], row['CtoAdq_USD'], row['ESTADO'], 
                            row['MODELO'])
            equipos.append(equipo)
        
        return equipos

    def menu(self):
        """Display a menu for user interaction to view equipment details."""
        while True:
            print("\nMenu:")
            print("1. Imprimir datos de un solo equipo")
            print("2. Imprimir datos de todos los equipos")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.imprimir_un_equipo()
            elif opcion == '2':
                self.imprimir_todos_los_equipos()
            elif opcion == '3':
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida, por favor intente de nuevo.")

    def imprimir_todos_los_equipos(self):
        """Print details of all equipment items."""
        if not self.equipos_vector:
            print("No hay equipos para mostrar.")
        else:
            for equipo in self.equipos_vector:
                print(equipo)

    def imprimir_un_equipo(self):
        """Print details of a specific equipment item identified by its ID."""
        equip_id = input("Ingrese el ID del equipo a imprimir: ")
        
        # Imprimir todos los IDs disponibles para depuración
        print("IDs disponibles:", [e.equip_id for e in self.equipos_vector])
        
        # Comprobar si el ID está presente
        equipo_encontrado = next((e for e in self.equipos_vector if str(e.equip_id) == str(equip_id)), None)
        
        if equipo_encontrado:
            print(equipo_encontrado)
        else:
            print("Equipo no encontrado.")

