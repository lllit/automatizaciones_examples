import speech_recognition as sr

# Todos los audios tienen que ser wav
filename = "data/audio.wav"
output_file = "transcripcion_audio.txt"

r = sr.Recognizer()

try:
    with sr.AudioFile(filename) as source:
        duration = int(source.DURATION) # solo permite maximo de 10 seg
        full_transcription = ""
        print("Procesando el archivo de audio...")
        for i in range(0, duration, 10):
            try:
                audio_data = r.record(source, duration=10)
                text = r.recognize_bing(audio_data, language="es-ES")
                full_transcription += text + "\n"
                print(f"Fragmento {i // 10 + 1}: {text}")

        
            except sr.UnknownValueError:
                print(f"Fragmento {i // 10 + 1}: No se pudo entender el audio.")
                full_transcription += "[No se pudo entender el audio]\n"


            except sr.RequestError as e:
                print(f"Error al comunicarse con el servicio de Google: {e}")
                break

        with open(output_file, 'w', encoding="utf-8") as f:
            f.write(full_transcription)                  

        print(f"Transcripcion completa y guardada en {output_file}")

except FileNotFoundError:
    print(f"El archivo {filename} no se encontró. Asegurate de que el archivo exista")
except ValueError as e:
    print(f"Error con el archivo de audio: {e}")
except Exception as e:
    print(f"Ocurrio un error inesperado: {e}")