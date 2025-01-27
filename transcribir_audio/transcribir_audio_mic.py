# import speech_recognition as sr
# import keyboard

# def listar_dispositivos():
#     dispositivos = sr.Microphone.list_microphone_names()
#     for index, name in enumerate(dispositivos):
#         print(f"{index}: {name}")


# def SpeechToText(device_index=None):
#     Ai = sr.Recognizer()
    

#     try:
#         with sr.Microphone(device_index=device_index) as source:
#             print("Hablando... Presiona 'q' para salir.")
#             listening = Ai.listen(source, phrase_time_limit=6)

#             try:

#                 command = Ai.recognize_bing(listening, language="es-ES")
#                 print("Has dicho: "+command)

#                 with open("transcripcion.txt", 'a', encoding="utf-8") as file:
#                     file.write(command+"\n")
        


#             except sr.UnknownValueError:
#                 print("No entendi lo que dijiste, intentemoslo de nuevo")

#     except AssertionError as e:
#         print(f"Error al inicializar el micrófono: {e}")


# if __name__ == "__main__":
#     print("Dispositivos disponibles:")
#     listar_dispositivos()
#     indice_mic = int(input("Elige el indice del microfono que deseas usar: "))

#     print("Presiona 'q' para salir en cualquier momento.")
#     while True:
#         if keyboard.is_pressed('q'):
#             print("Saliendo del programa...")
#             break
#         else:
#             SpeechToText(device_index=indice_mic)
        

import speech_recognition as sr
import keyboard

def listar_dispositivos():
    dispositivos = sr.Microphone.list_microphone_names()
    for index, name in enumerate(dispositivos):
        print(f"{index}: {name}")

def SpeechToText(device_index=None):
    Ai = sr.Recognizer()
    try:
        print(f"Intentando inicializar el micrófono con índice: {device_index}")
        with sr.Microphone(device_index=device_index) as source:
            print("Micrófono inicializado correctamente.")
            print("Hablando... Presiona 'q' para salir.")
            listening = Ai.listen(source, phrase_time_limit=6)

            try:
                command = Ai.recognize_bing(listening, language="es-ES")
                print("Has dicho: " + command)

                with open("transcripcion.txt", 'a', encoding="utf-8") as file:
                    file.write(command + "\n")

            except sr.UnknownValueError:
                print("No entendí lo que dijiste, intentémoslo de nuevo")
    except AssertionError as e:
        print(f"Error al inicializar el micrófono: {e}")
    except AttributeError as e:
        print(f"Error de atributo: {e}")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")

if __name__ == "__main__":
    print("Dispositivos disponibles:")
    listar_dispositivos()
    indice_mic = int(input("Elige el índice del micrófono que deseas usar: "))

    print("Presiona 'q' para salir en cualquier momento.")
    while True:
        if keyboard.is_pressed('q'):
            print("Saliendo del programa...")
            break
        else:
            SpeechToText(device_index=indice_mic)