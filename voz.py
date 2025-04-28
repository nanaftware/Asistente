import speech_recognition as sr

def grabar_texto():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = recognizer.listen(source)
    try:
        texto = recognizer.recognize_google(audio, language="es-ES")
        print(f"Tú dijiste: {texto}")
        return texto
    except sr.UnknownValueError:
        print("No se pudo entender el audio, intenta de nuevo.")
    except sr.RequestError as e:
        print(f"Error de servicio: {e}")
    return None
