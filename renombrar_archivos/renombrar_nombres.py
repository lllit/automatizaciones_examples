import os
from datetime import datetime

fecha_actual = datetime.now()
fecha_formateada = fecha_actual.strftime('%Y%m%d')

def rename_files(directory= "archivos", old_text = "Nuevo", new_text = fecha_formateada):

    for filename in os.listdir(directory):

        if old_text in filename:
            old_file = os.path.join(directory, filename)
            new_file_non = os.path.join(directory, filename.replace(old_text,new_text))
            os.rename(old_file, new_file_non)
            print(f"Archivo renombrado: {filename} -> {new_file_non}")
        else:

            rename_old = os.path.join(directory, filename)
            new_file = os.path.join(directory, filename.replace(filename,f"{new_text}_{filename}"))   


            os.rename(rename_old, new_file)
            print(f"Archivo renombrado: {filename} -> {new_file}")



# ---------- Ejemplos de usos -------------
#rename_files()

rename_files(old_text="Nuevo", new_text="Nuevo")