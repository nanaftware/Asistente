import subprocess
from audio import responder

def ejecutar(comando: str):
    try:
        if comando == "bloc de notas":
            subprocess.run("notepad", shell=True)
            responder("Abriendo el bloc de notas.")
        elif comando == "chrome":
            subprocess.run("start chrome", shell=True)
            responder("Abriendo Google Chrome.")
        elif comando == "brave":
            subprocess.run("start brave", shell=True)
            responder("Abriendo buscador Brave.")
        elif comando == "microsoft edge":   
            subprocess.run("start msedge", shell=True)
            responder("Abriendo Microsoft Edge.")
        elif comando == "explorador de archivos":
            subprocess.run("explorer", shell=True)
            responder("Abriendo el explorador de archivos.")
        elif comando == "calculadora":
            subprocess.run("calc", shell=True)
            responder("Abriendo la calculadora.")
        elif comando == "netflix":
            subprocess.run("start netflix", shell=True)
            responder("Abriendo Netflix.")
        elif comando in ("whatsapp", "telegram", "spotify"):
            subprocess.run(f"start {comando}", shell=True)
            responder(f"Abriendo {comando.capitalize()}.")
        elif comando == "apagar computadora":
            responder("Apagando la computadora.")
            subprocess.run("shutdown /s /t 1", shell=True)
        elif comando == "subir volumen":
            subprocess.run(
                'powershell -command "(New-Object -ComObject Wscript.Shell).' +
                'SendKeys([char]175)"', shell=True
            )
            responder("Subiendo el volumen.")
        elif comando == "bajar volumen":
            subprocess.run(
                'powershell -command "(New-Object -ComObject Wscript.Shell).' +
                'SendKeys([char]174)"', shell=True
            )
            responder("Bajando el volumen.")
        elif comando == "youtube":
            subprocess.run("start youtube", shell=True)
            responder("Abriendo YouTube.")
        else:
            responder("Comando no reconocido.")
    except Exception as e:
        print(f"Error al ejecutar comando: {e}")
        responder("Hubo un error al ejecutar el comando.")
