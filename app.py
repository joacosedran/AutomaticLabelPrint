import time
import typer
from rich.progress import Progress, SpinnerColumn, TextColumn
from InquirerPy import inquirer
from rich import print

def imprimir():
    with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
        ) as progress:
            progress.add_task(description="Imprimiendo...", total=None)
            time.sleep(5)
            print("Done!")

def listarDepartamento():
    print(f"Lista equipos por departamentos...")
    volver_menu()
def listaDispositivos():
    print("Imprimir lista de Netbooks...")
    volver_menu();
def imprimirEtiqueta():
    id = int(inquirer.text(message="Ingrese el id del equipo (Laptop/Pc)").execute())
    imprimir()
    print(f"Se imprimio la etiqueta {id}")
    volver_menu();

def volver_menu():
    inquirer.select(
        message="¿Quieres regresar al menú principal?",
        choices=["Sí", "No"]
    ).execute()
    menuOpciones()

def menuOpciones():
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
        listarDepartamento()
    if opcion_seleccionada == "listaDispositivos":
        listaDispositivos()
    if opcion_seleccionada == "imprimirEtiqueta":
        imprimirEtiqueta()
    if opcion_seleccionada == "salir":
        print("[magenta]Gracias por usar el programa[/magenta]. ¡Hasta luego!")
        raise typer.Exit()

def main():
    menuOpciones()
    
if __name__ == "__main__":
    typer.run(main)