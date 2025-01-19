import os
import shutil
from pathlib import Path
from datetime import datetime


def create_organization_folders(base_path):
    # Crea las carpetas necesarias para organizar los archivos
    folders = {
        'imagenes': ['.jpg', '.jpeg', '.png', '.gif', '.bpm'],
        'documentos': ['.pdf', '.doc', '.docx', '.txt', '.md'],
        'datasets': ['.xlsx', '.csv', '.sav'],
        'audio': ['.mp3', '.wav', '.flac', '.m4a'],
        'video': ['.mp4','.avi', '.mkv','.mov'],
        'comprimidos': ['.zip', '.rar', '.7z'],
        'otros': []
    }

    for folder in folders:
        folder_path = os.path.join(base_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    return folders



def get_folder_for_extension(extension, folders_dict):
    # Determina la carpeta correcta para una extension dada
    for folder, extensions in folders_dict.items():
        if extension.lower() in extensions:
            return folder
    return 'otros'

def organize_file(directory):
    # Organiza los archivos en el directorio especificado

    try:
        log = []
        directory = os.path.abspath(directory)
        folders = create_organization_folders(directory)
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)

            if os.path.isfile(file_path) and not filename.startswith('.'):
                # obtener extension
                extension = os.path.splitext(filename)[1]

                # determinar la carpeta destino
                dest_folder = get_folder_for_extension(extension, folders)
                destination = os.path.join(directory, dest_folder,filename)

                try:
                    shutil.move(file_path, destination)
                    log.append(f"Movido {filename} -> {dest_folder}/")
                except Exception as e:
                    log.append(f"Error al mover {filename}: {str(e)}")

        if log:
            print("\n=== Reporte de Organizacion ===")
            print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Directorio: {directory}")
            print("\nMovimientos realizados:")
            for entry in log:
                print(f"- {entry}")
        else:
            print("No se encontraron archivos para organizar")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    # Solicitar directorio
    directory = input("Ingrese la ruta del directorio a organizar (Enter para directorio actual): ").strip()

    if not directory:
        directory = "."
    
    if not os.path.exists(directory):
        print("Error: El directorio especificado no existe.")
        exit(1)

    print(f"\nSe organizaran los archivos en: {os.path.abspath(directory)}")
    confirm = input("¿Desea continuar? (s/n): ")

    if confirm.lower() == 's':
        organize_file(directory)
    else:
        print("Operacion cancelada!")
    