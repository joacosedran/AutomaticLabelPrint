from class_equipos import Equipos

class Ingenieria(Equipos):
    def ruta():
        RUTA_INGE = "EquiposCremona.xlsx"  # Replace with the actual path
        SHEET_INGE = "Ingenieria"          # Replace with your actual sheet name

        gestor = GestorEquipos(RUTA_INGE, SHEET_INGE)# Create an instance
        
        return gestor