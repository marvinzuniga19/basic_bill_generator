import os
import openpyxl

# Obtener la ruta de la carpeta "Documentos"
documents_path = os.path.join(os.path.expanduser('~'), 'Documentos')

# Crear un nuevo libro de Excel
workbook = openpyxl.Workbook()

# Seleccionar la hoja activa
sheet = workbook.active

# Agregar encabezados a las columnas
sheet['A1'] = 'Fecha'
sheet['B1'] = 'Concepto'
sheet['C1'] = 'Monto'

# Agregar datos al recibo
sheet['A2'] = '26/04/2023'
sheet['B2'] = 'Pago de renta'
sheet['C2'] = 1500

# Guardar el archivo Excel en la carpeta "Documentos"
filename = os.path.join(documents_path, 'recibo.xlsx')
workbook.save(filename)
