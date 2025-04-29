import os
import threading
from io import BytesIO
from gtts import gTTS
import pygame

_audio_file = "respuesta.mp3"
play_event = threading.Event()  # Señal para indicar reproducción en curso

def init_mixer():
    if not pygame.mixer.get_init():
        pygame.mixer.init()

def _reproducir(texto: str):
    """Genera y reproduce audio desde memoria, sin bloquear la escucha."""
    try:
        play_event.set() # Desactivar escucha :contentReference[oaicite:8]{index=8}
        init_mixer() # Generar audio en archivo temporal
        tts = gTTS(texto, lang="es")
        tts.save(_audio_file) # Cargar en memoria
        with open(_audio_file, "rb") as f:
            data = BytesIO(f.read())
        sound = pygame.mixer.Sound(data) # Carga desde buffer :contentReference[oaicite:9]{index=9}
        sound.play()
        while pygame.mixer.get_busy():
            pygame.time.Clock().tick(10)
    finally:
        pygame.mixer.quit()
        if os.path.exists(_audio_file):
            os.remove(_audio_file) # Ya se puede borrar sin bloqueo :contentReference[oaicite:10]{index=10}
        play_event.clear() # Reactivar escucha

def responder(texto: str):
    """Lanza la reproducción en un hilo demonio para no bloquear."""
    hilo = threading.Thread(target=_reproducir, args=(texto,), daemon=True)
    hilo.start() # Demonio termina con el programa :contentReference[oaicite:11]{index=11}

def detener():
    """Detiene la reproducción en curso y limpia recursos."""
    if pygame.mixer.get_init():
        pygame.mixer.stop()
        pygame.mixer.quit()
    if os.path.exists(_audio_file):
        os.remove(_audio_file)
    play_event.clear()
