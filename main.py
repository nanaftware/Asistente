# import respuestas 
from audio import responder, detener, play_event
from voz import grabar_texto
from mensajes import saludo_inicio, saludo_despedir, NO_ENTENDIDO
from comandos import comandos_dict
from comando import ejecutar
from busqueda import buscar_y_abrir

def main():
    responder(saludo_inicio())

    while True:
        # Si estamos reproduciendo audio, esperamos
        if play_event.is_set():
            continue  # saltamos grabar_texto() hasta que termine el TTS :contentReference[oaicite:2]{index=2}

        texto = grabar_texto()
        if not texto:
            responder(NO_ENTENDIDO)
            continue

        accion = comandos_dict.get(texto)
        if accion == "detener":
            detener()
            continue
        if accion == "aplicacion":
            ejecutar(texto)
            continue
        if texto in ("salir","terminar","adiós","cerrar"):
            responder(saludo_despedir())
            break

        # Búsqueda en línea
        respuesta = buscar_y_abrir(texto)
        responder(respuesta)

    detener()

if __name__ == "__main__":
    main()
