import PyPDF2
import re
import os

# Esta funcion por ahora extrae todos los datos de los PDF  
def extract_invoice_info(pdf_file_path):
    with open(pdf_file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        text = ''

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        print(text)
 
extract_invoice_info("./data/Ver_Facturas.pdf")