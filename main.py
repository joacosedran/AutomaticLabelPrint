from class_gestor_equipos import GestorEquipos
from funciones import main
import typer

"""
if __name__ == "__main__":
    RUTA_INGE = "Ingenieria.xlsx"  # Actualiza con la ruta de tu archivo
    SHEET_INGE = "Sheet1"           # Actualiza con el nombre de tu hoja

    gestor = GestorEquipos(RUTA_INGE, SHEET_INGE)
    
    # Iniciar el menú
    gestor.menu()
"""

if __name__ == "__main__":
    # Run the menu
    typer.run(main)