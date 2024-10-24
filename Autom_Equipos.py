from class_gestor_equipos import GestorEquipos

if __name__ == "__main__":
    RUTA_INGE = "Ingenieria.xlsx"  # Actualiza con la ruta de tu archivo
    SHEET_INGE = "Sheet1"           # Actualiza con el nombre de tu hoja

    gestor = GestorEquipos(RUTA_INGE, SHEET_INGE)
    
    # Iniciar el menú
    gestor.menu()
