import subprocess
from audio import responder

def ejecutar_comando(comando):
    try:
        # aplicaciones
        if comando == "bloc de notas":
            subprocess.run("notepad", shell=True)
            responder("Abriendo el bloc de notas.")
        elif comando == "chrome":
            subprocess.run("start chrome", shell=True)
            responder("Abriendo Google Chrome.")
        elif comando == "brave":
            subprocess.run("start brave", shell=True)
            responder("Abriendo buscador Brave.")
        elif comando == "whatsapp":
            subprocess.run("start whatsapp", shell=True)
            responder("Abriendo WhatsApp.")
        elif comando == "telegram":
            subprocess.run("start telegram", shell=True)
            responder("Abriendo Telegram.")
        elif comando == "spotify":
            subprocess.run("start spotify", shell=True)
            responder("Abriendo Spotify.")
        # apagar
        elif comando == "apagar computadora":
            responder("Apagando la computadora.")
            subprocess.run("shutdown /s /t 1", shell=True)
        # volumen
        elif comando == "subir volumen":
            subprocess.run(
                'powershell -command "(New-Object -ComObject Wscript.Shell).SendKeys([char]175)"', shell=True
            )
            responder("Subiendo el volumen papi chulo.")
        elif comando == "bajar volumen":
            subprocess.run(
                'powershell -command "(New-Object -ComObject Wscript.Shell).SendKeys([char]174)"', shell=True
            )
            responder("Bajando el volumen bonito.")
        else:
            responder("Comando no reconocido.")
    except Exception as e:
        print(f"Error al ejecutar el comando: {e}")
        responder("Hubo un error al ejecutar el comando.")
