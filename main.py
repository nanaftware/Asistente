# import respuestas 
from audio import responder, detener, play_event
from voz import grabar_texto
from mensajes import saludo_inicio, saludo_despedir, NO_ENTENDIDO
from comandos import comandos_dict
from comando import ejecutar
from busqueda import buscar_y_abrir
from llm import preguntar_al_llm, limpiar_historial

def main():
    responder(saludo_inicio())
    while True:
        # Si estamos reproduciendo audio, esperamos
        if play_event.is_set():
            continue  # saltamos grabar_texto() hasta que termine el TTS

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

        if texto in ("salir", "terminar", "adiós", "cerrar"):
            limpiar_historial()
            responder(saludo_despedir())
            break

        # Primero intenta búsqueda/comandos rápidos
        respuesta = buscar_y_abrir(texto)

        # Si no encontró nada útil, pregunta al LLM
        if not respuesta or "no encontré" in respuesta.lower():
            respuesta = preguntar_al_llm(texto)

        responder(respuesta)  # ← dentro del while

    detener()  # ← fuera del while, se ejecuta al salir

if __name__ == "__main__":
    main()
