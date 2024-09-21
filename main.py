from openpyxl import load_workbook
from web_scaping import *


file_xlsx = "plantilla.xlsx"
sheet_xlsx = "Hoja1"

# # Cargar el archivo Excel
# workbook = load_workbook(filename=file_xlsx)

# # Seleccionar la hoja
# hoja = workbook[sheet_xlsx]

# # Asignar un valor a la celda B1
# hoja["B1"] = "Nuevo Valor"

# # Guardar los cambios en el archivo
# workbook.save(filename=file_xlsx)

# print("Valor asignado a la celda B1.")

scraping = Swp_page()
scraping.gold_prices()