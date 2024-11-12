import win32print
import win32ui
import win32con
from PIL import Image, ImageWin

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')

def imprimir_etiqueta(equipos_vector):
    printer_name = "Departamento De Sistemas"
    hprinter = win32print.OpenPrinter(printer_name)
    try:
        hdc = win32ui.CreateDC()
        hdc.CreatePrinterDC(printer_name)
        hdc.SetMapMode(win32con.MM_LOMETRIC)

        ancho_mm = 1000
        alto_mm = 600
        hdc.SetWindowExt((ancho_mm, alto_mm))

        hdc.StartDoc("Etiquetas de Equipos")
        
        # Define la posición inicial de la primera etiqueta
        
        font_name = "Arial"
        font_size = 45
        font_weight = win32con.FW_BOLD
        hfont = win32ui.CreateFont({
            "name": font_name,
            "height": font_size,
            "weight": font_weight,
        })
        hdc.SelectObject(hfont)

        # Imprimir cada equipo en equipos_vector
        for equipo in equipos_vector:
            hdc.StartPage()
            
            y_offset = -50
            hdc.TextOut(25, y_offset, f"ID: {equipo.tipo} - {equipo.departamento} - {equipo.equip_id}")
            y_offset -= 50
            hdc.TextOut(25, y_offset, f"Usuarios: {equipo.usuarios}")
            y_offset -= 50
            hdc.TextOut(25, y_offset, f"Estado: {equipo.estado}")
            
            # Cargar la imagen y eliminar la transparencia agregando un fondo blanco
            image_path = "IMG/creminox2.png"
            image = Image.open(image_path).convert("RGBA")  # Asegúrate de que la imagen tenga el modo RGBA
            fondo_blanco = Image.new("RGBA", image.size, (255, 255, 255, 255))  # Fondo blanco en modo RGBA

            # Componer la imagen con el fondo blanco
            imagen_con_fondo = Image.alpha_composite(fondo_blanco, image).convert("RGB")

            # Redimensionar la imagen con fondo blanco
            nuevo_ancho = 328  # Define el nuevo ancho en píxeles
            nuevo_alto = 80  # Define el nuevo alto en píxeles
            imagen_redimensionada = imagen_con_fondo.resize((nuevo_ancho, nuevo_alto), Image.LANCZOS)

            # Rotar y reflejar la imagen para la orientación deseada
            imagen_rotada = imagen_redimensionada.rotate(180)
            imagen_reflejada = imagen_rotada.transpose(Image.FLIP_LEFT_RIGHT)

            # Convertir la imagen redimensionada y rotada a un formato compatible para imprimir
            dib = ImageWin.Dib(imagen_reflejada)

            # Definir la posición para imprimir la imagen en la esquina inferior derecha
            x = 660  # posición x
            y = -550 # posición y

            # Dibujar la imagen en el contexto de la impresora
            dib.draw(hdc.GetHandleOutput(), (x, y, x + nuevo_ancho, y + nuevo_alto))
            
            hdc.EndPage()  # Finaliza la página para el equipo actual
            
        hdc.EndDoc()  # Termina el documento después de imprimir todos los equipos

    finally:
        win32print.ClosePrinter(hprinter)
