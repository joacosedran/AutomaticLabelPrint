
# Clase por Departamento

Se propone que cada departamento tenga una clase propia, cada uno heredando los atributos de una clase "Equipo" la cual heredara todos sus atributos (datos) para reutilizar codigo, como ejemplo:

```bash
def cargar_datos(self, ruta_inge, sheet_inge):
        [carga de datos]

class Equipos:
    def __init__(self, equip_id, tipo, os, marca, usuarios, antiguedad, gama, disco, cto_adq_usd, estado, modelo):
        self.equip_id = equip_id
        self.tipo = tipo
        self.os = os
        ...
        ..
        .

    def __repr__(self):
        return (f"ID: {self.equip_id}, Tipo: {self.tipo}, OS: {self.os}, Marca: {self.marca}, "
                f"Usuarios: {self.usuarios}, Antigüedad: {self.antiguedad}, Gama: {self.gama}, "
                f"Disco: {self.disco}, Cto Adq (USD): {self.cto_adq_usd}, Estado: {self.estado}, "
                f"Modelo: {self.modelo}")
    
    def ruta():
        return
    
class Ingenieria(Equipos):
    def ruta:
        gestor = GestorEquipos(RUTA_INGE, SHEET_INGE)
        return gestor

class Produccion(Equipos):
    def ruta:
        SHEET_INGE = "Produccion"
        gestor = GestorEquipos(RUTA_INGE, SHEET_INGE)# Create an instance
        return gestor

clas Administracion(Equipos):
    def ruta:
        SHEET_INGE = "Administracion"
        gestor = GestorEquipos(RUTA_INGE, SHEET_INGE)
        return gestor
```

En cada una de estas clases se cargaran los datos de sus respectivos dispositivos.

------------------------------------------------------------------------------------------------------------------
# Separar archivos por carpetas

Al querer separar los archivos por carpetas y ejecutar nos muestra este error:

```bash
Traceback (most recent call last):
  File "d:\ZZ-Codes\AutomaticLabelPrint\main.py", line 1, in <module>
    from Funciones.Funciones import main
  File "d:\ZZ-Codes\AutomaticLabelPrint\Funciones\Funciones.py", line 4, in <module>
    from ..Clases.Clase_Equipos import Equipos
ImportError: attempted relative import beyond top-level package
```


## Solucion

Esto se soluciona agregando al archivo "Funciones\Funciones.py" estas lineas:
```bash
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')

from Clases.Clase_Equipos import Equipos
```
Solucion que no me gusta, pero funciona, ya se vera como mejorarlo y optimizarlo.

Asegurate de que cada carpeta (proyecto, clases, funciones) contenga un archivo __init__.py (aunque este vacio). Esto le indica a Python que trate a cada carpeta como un paquete.

------------------------------------------------------------------------------------------------------------------------------

Se creo por fin un entorno virtual donde se podran descargar todos los requerimientos sin que estos se descarguen globalmente, no se muy bien si se agrega al git o si hay que hacerlo cada que se vuelve a abrir el visual studio code.

------------------------------------------------------------------------------------------------------------------------------

Se requiere imprimir en la etiqueta la ubicacion del equipo, una opcion es agregar al objeto un atributo llamado "ubicacion", el cual cargaremos desde el constructor.