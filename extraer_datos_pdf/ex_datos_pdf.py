from docling.document_converter import DocumentConverter

source = "./data/example2.pdf" # Document
converter = DocumentConverter()
result = converter.convert(source)

data = result.document.export_to_dict()

def extract_value(texts, key):
    for i, item in enumerate(texts):
        #print("Text ",item["text"])
        #print("KEY: ",key)
        if item["text"] == key and i + 1 < len(texts):
            return texts[i + 1]["text"]
    return None

#print(data['texts'][1]['text'])

#codigo_verificacion = extract_value(data['texts'], 'CERTIFICADO DE T"TULO TÉCNICO PROFESIONAL')

#print(codigo_verificacion)

#incoice_number = extract_value(data["texts"], "Incoice Number")


# ----------------------
def extract_values_pdf(texts, key):
    values = []
    for i, item in enumerate(texts):
        if key.lower() in item["text"].lower():
            values.append(item["text"])
    return values

# Ejemplo de uso
nombre_titulo = extract_values_pdf(data['texts'], 'CERTIFICADO')
detalle_titulo = extract_values_pdf(data['texts'],'Certifico que don')
nivel_titulo = extract_values_pdf(data['texts'], 'El referido Título')
codigo_verificacion = extract_values_pdf(data['texts'],"Código de Verificación")


print("Titulo: " ,nombre_titulo)
print("Detalle: " , detalle_titulo)
print("Nivel titulo: ", nivel_titulo)
print("Codigo de Verificacion", codigo_verificacion)