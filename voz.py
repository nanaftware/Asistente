import speech_recognition as sr
from speech_recognition import WaitTimeoutError

def grabar_texto(timeout: float = 5, phrase_time_limit: float = 3) -> str | None:
    """
    Captura audio y devuelve el texto en minúsculas,
    o None si ocurre un timeout o error.
    """
    r = sr.Recognizer()
    with sr.Microphone() as src:
        # Umbral alto para ignorar el TTS
        r.energy_threshold = 4000
        r.dynamic_energy_threshold = True
        r.adjust_for_ambient_noise(src, duration=0.5)

        print("Escuchando...")
        try:
            audio = r.listen(src, timeout=timeout, phrase_time_limit=phrase_time_limit)
        except WaitTimeoutError:
            print("Timeout: nadie habló.")  # Evita la excepción cruda
            return None

    try:
        texto = r.recognize_google(audio, language="es-ES")
        return texto.strip().lower()
    except sr.UnknownValueError:
        print("No se pudo entender el audio.")
    except sr.RequestError as e:
        print(f"Error servicio reconocimiento: {e}")
    return None
