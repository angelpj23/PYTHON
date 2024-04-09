# -*- coding: utf-8 -*-
# La declaracion de utf es necesaria
import openpyxl

def reemplazar_letras(nombre_archivo):
    nombre_archivo = "ventas-mtro-2024.xls"
    # Abre el archivo Excel
    libro_excel = openpyxl.load_workbook(nombre_archivo)
    hoja = libro_excel.active

    # Recorre cada celda y reemplaza la letra original por la nueva
    for fila in hoja.iter_rows():
        for celda in fila:
            if isinstance(celda.value, str):
                celda.value = celda.value.replace("Ã³", "ó")

    # Guarda los cambios en el mismo archivo
    libro_excel.save(nombre_archivo)
    print("Reemplazo completado.")