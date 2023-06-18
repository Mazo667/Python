from PyPDF2 import PdfReader

reader = PdfReader("/home/maximiliano/Escritorio/UDC/1er Cuatrimestre/Introduccion a la Programacion/Practico 2 2022.pdf")
page = reader.pages[0]
print(page.extract_text())