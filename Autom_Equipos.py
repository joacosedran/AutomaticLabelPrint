import pandas as pd
from Class_Equipos import Equipos

# Cargar los datos desde el archivo Excel
df = pd.read_excel("Ingenieria.xlsx", sheet_name="Sheet1")

# Crear una lista para almacenar los objetos
equipos_vector = []

# Iterar sobre las filas del DataFrame
for index, row in df.iterrows():
    # Crear un objeto Equipos para cada fila
    equipo = Equipos(row['ID'], row['TIPO'], row['OS'], row['MARCA'], row['USUARIOS'], row['ANTIGUEDAD'], row['GAMA'], row['DISCO'], row['CtoAdq_USD'], row['ESTADO'], row['MODELO'])
    equipos_vector.append(equipo)

# Mostrar los objetos creados
print(equipos_vector)
