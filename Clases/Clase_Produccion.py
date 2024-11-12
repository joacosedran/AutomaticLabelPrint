from .Clase_Equipos import Equipos

class Produccion(Equipos):
    HOJA = "Equipos Activos - Dep. Prod."

    def __init__(self, equip_id, tipo, os, marca, usuarios, antiguedad, gama, disco, estado, modelo):
        super().__init__(equip_id, tipo, os, marca, usuarios, antiguedad, gama, disco, estado, modelo)
        self.ubicacion = "Produccion"