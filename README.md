# Proyecto de Impresión de Etiquetas para Computadoras

Este proyecto, desarrollado en Python, automatiza la impresión de etiquetas para equipos de cómputo a partir de un registro en un archivo de Excel. Es ideal para generar etiquetas consistentes y rápidamente accesibles para el inventario de computadoras.

## Características

- **Lectura de datos en Excel**: Extrae datos de un archivo de Excel en el cual se encuentran los registros de cada computadora.
- **Impresión de etiquetas**: Formatea e imprime etiquetas de acuerdo con la información especificada en el archivo de registro.
- **Automatización eficiente**: Minimiza el tiempo requerido para el etiquetado y evita errores manuales.

## Requisitos

- **Python 3.8+**
- **Bibliotecas**:
  - `pandas`: Para manipular datos en el archivo Excel.
  - `openpyxl`: Para leer y escribir archivos en formato Excel.
  - `win32print` y `win32api`: Para gestionar la impresora en sistemas Windows.

Instala las dependencias con el siguiente comando:

```bash
pip install typer InquirerPy time
