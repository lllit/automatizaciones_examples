import json
import pyperclip
import sys
import time
import win32gui
import win32process
import psutil
from datetime import datetime


def get_activate_window_process_name():
    """
    Obtiene el nombre del proceso de la ventana activa
    """
    try:
        window = win32gui.GetForegroundWindow()
        _, pid = win32process.GetWindowThreadProcessId(window)
        process = psutil.Process(pid)

        return process.name().replace(".exe", "")
    except:
        return "Unknown"

def save_clipboard(data_file):
    """
    Guarda el contenido actual del portapapeles con una clave
    """
    try:
        with open(data_file, 'r') as f:
            clipboard_data = json.load(f)

    except (FileNotFoundError, json.JSONDecodeError):
        clipboard_data = {}
        
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    app_name = get_activate_window_process_name()
    key = f"{app_name}_{timestamp}"

    clipboard_data[key] = pyperclip.paste()

    with open(data_file, 'w') as f:
        json.dump(clipboard_data, f)

    print(f"Datos Guardados de: {key}")

def load_clipboard(data_file, key):
    # Guarda el contenido del portapapeles usando clave
    try:
        with open(data_file, 'r') as f:
            clipboard_data = json.load(f)
            if key in clipboard_data:
                pyperclip.copy(clipboard_data[key])
                print(f"Datos de '{key}' copiados al portapapeles")
            else:
                print(f"Clave '{key}' no encontrada")

    except FileNotFoundError:
        print("No se encontraron datos guardados")
    
def monitor_clipboard():
    # Monitorea continuemanete el portapapeles y guarda su contenido

    data_file = "clipboard_data.json"
    last_value = pyperclip.paste()
    print("Monitoreando el portapapeles... (Presiona Ctrl+C para detener)")

    try:
        while True:
            current_event = pyperclip.paste()
            if current_event != last_value:
                #app_name = get_activate_window_process_name()
                save_clipboard(data_file)
                last_value = current_event
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nMonitoreo detenido")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        monitor_clipboard()
    elif len(sys.argv) == 3:
        data_file = "clipboard_data.json"
        command = sys.argv[1].lower()
        key = sys.argv[2]

        if command == "save":
            save_clipboard(data_file, key)
        elif command == "load":
            load_clipboard(data_file, key)
    else:
        print("Uso:")
        print(" Para monitoreo automatico:")
        print("     python multi_clipboard.py")
        print(" Para uso manual:")
        print("     python multi_clipboard.py [save/load] [key]")