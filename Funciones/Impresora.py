import win32print
import win32ui
import win32con
from PIL import Image, ImageWin  # Asegúrate de importar ImageWin

# Nombre de la impresora
printer_name = "SATO WS408"

# Abrir la impresora
hprinter = win32print.OpenPrinter(printer_name)

try:
    # Crear el contexto de dispositivo para la impresora
    hdc = win32ui.CreateDC()
    hdc.CreatePrinterDC(printer_name)

    # Configurar el modo de mapeo a MM_LOMETRIC (décimas de milímetro)
    hdc.SetMapMode(win32con.MM_LOMETRIC)

    # Establecer el tamaño de la ventana para que coincida con el tamaño de la etiqueta (décimas de mm)
    ancho_mm = 1000  # 100 mm = 1000 décimas de milímetro
    alto_mm = 600    # 60 mm = 600 décimas de milímetro
    hdc.SetWindowExt((ancho_mm, alto_mm))

    # Inicia un documento de impresión
    hdc.StartDoc("Etiqueta de Prueba con Imagen")
    hdc.StartPage()

    # Definir y crear la fuente
    font_name = "Arial"
    font_size = 45
    font_weight = win32con.FW_BOLD

    hfont = win32ui.CreateFont({
        "name": font_name,
        "height": font_size,
        "weight": font_weight,
    })

    # Seleccionar la fuente en el contexto de la impresora
    hdc.SelectObject(hfont)

    # Imprimir texto en la parte superior de la etiqueta
    hdc.TextOut(25, -50, "ID: 912018")
    hdc.TextOut(25, -100, "Nombre: ")
    hdc.TextOut(25, -150, "Ubicación: ")
    hdc.TextOut(25, -200, "Estado: ")
    hdc.TextOut(25, -250, "Número de serie: ")

    # Cargar la imagen
    image_path = "C:/Users/s_pasante/Desktop/sdsdsa/AutomaticLabelPrint/IMGCREMI.jpg"  # Reemplaza con la ruta de tu imagen
    image = Image.open(image_path).convert("RGB")
    
        # Redimensionar la imagen
    nuevo_ancho = 200  # Define el nuevo ancho en píxeles
    nuevo_alto = 200  # Define el nuevo alto en píxeles
    imagen_redimensionada = image.resize((nuevo_ancho, nuevo_alto), Image.LANCZOS)

    # Convertir la imagen a un formato compatible para imprimir
    dib = ImageWin.Dib(image)
    

    # Definir la posición para imprimir la imagen
    x = 100   # posición x
    y = -500 # posición y (ajusta según sea necesario)

    # Dibujar la imagen en el contexto de la impresora
    dib.draw(hdc.GetHandleOutput(), (x, y, x + image.width, y + image.height))

    # Finalizar la impresión
    hdc.EndPage()
    hdc.EndDoc()

finally:
    win32print.ClosePrinter(hprinter)  # Asegurarse de cerrar la impresora
