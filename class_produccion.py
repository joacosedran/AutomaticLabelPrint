from class_equipos import Equipos

class Produccion(Equipos):
    def ruta():
        SHEET_INGE = "Produccion"          # Replace with your actual sheet name

        gestor = GestorEquipos(RUTA_INGE, SHEET_INGE)# Create an instance
        
        return gestor