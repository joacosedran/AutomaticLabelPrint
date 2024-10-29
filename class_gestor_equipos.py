import pandas as pd
from class_equipos import Equipos

class GestorEquipos:
    def __init__(self, ruta_inge, sheet_inge):
        self.equipos_vector = self.cargar_datos(ruta_inge, sheet_inge)

    def cargar_datos(self, ruta_inge, sheet_inge):
        df = pd.read_excel(ruta_inge, sheet_name=sheet_inge)
        equipos = []
        
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
        if not self.equipos_vector:
            print("No hay equipos para mostrar.")
        else:
            for equipo in self.equipos_vector:
                print(equipo)

    def imprimir_un_equipo(self):
        equip_id = input("Ingrese el ID del equipo a imprimir: ")
        
        print("IDs disponibles:", [e.equip_id for e in self.equipos_vector])
        
        equipo_encontrado = next((e for e in self.equipos_vector if str(e.equip_id) == str(equip_id)), None)
        
        if equipo_encontrado:
            print(equipo_encontrado)
        else:
            print("Equipo no encontrado.")

