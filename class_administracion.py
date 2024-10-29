from class_equipos import Equipos

class Administracion(Equipos):
    def ruta():
        RUTA_INGE = "EquiposCremona.xlsx"  # Replace with the actual path
        SHEET_INGE = "Administracion"      # Replace with your actual sheet name

        gestor = GestorEquipos(RUTA_INGE, SHEET_INGE)# Create an instance
        
        return gestor