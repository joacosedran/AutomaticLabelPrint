from .Clase_Equipos import Equipos

class Administracion(Equipos):
    HOJA = "Equipos Activos - Dep. Adm."

    def __init__(self, equip_id, tipo, os, marca, usuarios, antiguedad, gama, disco, estado, modelo):
        super().__init__(equip_id, tipo, os, marca, usuarios, antiguedad, gama, disco, estado, modelo)
        self.ubicacion = "Administracion"