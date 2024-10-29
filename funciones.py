import time
import pandas as pd
import typer
from class_equipos import Equipos
from rich.progress import Progress, SpinnerColumn, TextColumn
from InquirerPy import inquirer
from rich import print

class GestorEquipos:

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

    def menuOpciones(self):
        """Display a menu for user interaction to view equipment details."""
        opciones = [
            {"name": "1 Imprimir etiquetas por Departamento", "value":"listarDepartamento"},
            {"name": "2 Imprimir etiquetas por Dispositivo", "value":"listaDispositivos"},
            {"name": "3 Imprimir una etiqueta", "value":"imprimirEtiqueta"},
            {"name": "Salir", "value": "salir"}
        ]
        opcion_seleccionada = inquirer.select(
            message="Selecciona una opción:",
            choices=opciones,
            pointer="♦️ ",
        ).execute()

        if opcion_seleccionada == "listarDepartamento":
            self.imprimir_un_equipo()
        if opcion_seleccionada == "listaDispositivos":
            self.imprimir_todos_los_equipos()
        if opcion_seleccionada == "imprimirEtiqueta":
            print("Saliendo del programa.")
        if opcion_seleccionada == "salir":
            print("[magenta]Gracias por usar el programa[/magenta]. ¡Hasta luego!")
            raise typer.Exit()
        
    def imprimir_todos_los_equipos(self):
        """Print details of all equipment items."""
        if not self.equipos_vector:
            print("No hay equipos para mostrar.")
        else:
            for equipo in self.equipos_vector:
                print(equipo)
        GestorEquipos.volver_menu();

    def imprimir_un_equipo(self):
        """Print details of a specific equipment item identified by its ID."""
        
        # Imprimir todos los IDs disponibles para depuración
        print("IDs disponibles:", [e.equip_id for e in self.equipos_vector])
        
        equip_id = input("Ingrese el ID del equipo a imprimir: ")
        
        # Comprobar si el ID está presente
        equipo_encontrado = next((e for e in self.equipos_vector if str(e.equip_id) == str(equip_id)), None)
        
        if equipo_encontrado:
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                transient=True,
            ) as progress:
                progress.add_task(description="Imprimiendo...", total=None)
                time.sleep(5)
                print("Done!")
        else:
            print("Equipo no encontrado.")
        GestorEquipos.volver_menu();
            
    def volver_menu():
        option_selected = inquirer.select(
            message="¿Quieres regresar al menú principal?",
            choices=["Y", "N"]
        ).execute()
        if option_selected == "Y":
            GestorEquipos.menuOpciones();
        else:
            close_program()
    
def main():
    RUTA_INGE = "Ingenieria.xlsx"  # Replace with the actual path
    SHEET_INGE = "Sheet1"          # Replace with your actual sheet name

    gestor = GestorEquipos(RUTA_INGE, SHEET_INGE)# Create an instance
    gestor.menuOpciones()     # Call the menuOpciones method on the instance
    
def close_program():
    print("Gracias por usar nuestro programa.")