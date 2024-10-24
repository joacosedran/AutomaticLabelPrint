import win32print
import win32ui

# Nombre de la impresora que configuraste en el sistema operativo
printer_name = "Departamento De Sistemas" 

# Crear un contexto de impresión
hprinter = win32print.OpenPrinter(printer_name)

try:
    # Crear un DC para la impresora
    hdc = win32ui.CreateDC()
    hdc.CreatePrinterDC(printer_name)  # Cambié esta línea para usar CreatePrinterDC

    hdc.StartDoc("Documento de Prueba")
    hdc.StartPage()

    # Imprimir texto en la página
    hdc.TextOut(100, 100, "Texto de prueba en la impresora SATO WS408")

    hdc.EndPage()
    hdc.EndDoc()
finally:
    win32print.ClosePrinter(hprinter)
