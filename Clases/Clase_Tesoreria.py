from .Clase_Equipos import Equipos

class Tesoreria(Equipos):
    HOJA = "Equipos Activos - Ofic. Tesor."

    def __init__(self, equip_id, tipo, os, marca, usuarios, antiguedad, gama, disco, estado, modelo):
        super().__init__(equip_id, tipo, os, marca, usuarios, antiguedad, gama, disco, estado, modelo)
        self.ubicacion = "Tesoreria"