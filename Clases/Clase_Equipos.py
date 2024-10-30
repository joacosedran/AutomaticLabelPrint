class Equipos:
    RUTA = "Excel/Equipos.xlsx"
    def __init__(self, equip_id, tipo, os, marca, usuarios, antiguedad, gama, disco, cto_adq_usd, estado, modelo):
        self.equip_id = equip_id
        self.tipo = tipo
        self.os = os
        self.marca = marca
        self.usuarios = usuarios
        self.antiguedad = antiguedad
        self.gama = gama
        self.disco = disco
        self.cto_adq_usd = cto_adq_usd
        self.estado = estado
        self.modelo = modelo

    def __repr__(self):
        return (f"ID: {self.equip_id}, Tipo: {self.tipo}, OS: {self.os}, Marca: {self.marca}, "
                f"Usuarios: {self.usuarios}, Antigüedad: {self.antiguedad}, Gama: {self.gama}, "
                f"Disco: {self.disco}, Cto Adq (USD): {self.cto_adq_usd}, Estado: {self.estado}, "
                f"Modelo: {self.modelo}")