class Equipos:
    def __init__(self, ID, TIPO, MODELO, OS, MARCA, USUARIOS, ANTIGUEDAD, GAMA, DISCO, CtoAdq_USD, ESTADO):
        self.ID = ID
        self.TIPO = TIPO
        self.MODELO = MODELO
        self.OS = OS
        self.MARCA = MARCA
        self.USUARIOS = USUARIOS
        self.ANTIGUEDAD = ANTIGUEDAD
        self.GAMA = GAMA
        self.DISCO = DISCO
        self.CtoAdq_USD = CtoAdq_USD
        self.ESTADO = ESTADO

    def __repr__(self):
        return f"Equipos(ID = {self.ID}, TIPO = {self.TIPO}, OS = {self.MARCA}, USUARIOS = {self.USUARIOS}, ANTIGUEDAD = {self.ANTIGUEDAD}, GAMA = {self.USUARIOS}, DISCO = {self.DISCO}, Cto_Adq_USD = {self.CtoAdq_USD}, ESTADO = {self.ESTADO}, MODELO = {self.MODELO})"
