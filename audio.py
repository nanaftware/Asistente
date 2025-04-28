import os
from gtts import gTTS
import pygame

audio_file = "respuesta.mp3"

def init_mixer():
    if not pygame.mixer.get_init():
        pygame.mixer.init()

def responder(texto):
    init_mixer()
    # limpia cualquier archivo previo
    if os.path.exists(audio_file):
        os.remove(audio_file)

    tts = gTTS(texto, lang="es")
    tts.save(audio_file)
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    clock = pygame.time.Clock()
    while pygame.mixer.music.get_busy():
        clock.tick(10)
    pygame.mixer.music.stop()
    pygame.mixer.quit()

    if os.path.exists(audio_file):
        os.remove(audio_file)

def detener():
    if pygame.mixer.get_init():
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        pygame.mixer.quit()
    if os.path.exists(audio_file):
        os.remove(audio_file)
