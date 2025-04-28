from mensajes import saludo_inicio, saludo_despedir
from comandos import comandos_aplicaciones, comandos_detener
from voz import grabar_texto
from audio import responder, detener
from comando import ejecutar
from busqueda import buscar_y_abrir
# import respuestas 


def main():
    responder(saludo_inicio())

    while True:
        texto = grabar_texto()
        if not texto:
            continue
        texto = texto.strip().lower()

        if texto in comandos_detener:
            detener()
            continue

        if texto in ["salir", "terminar", "adiós", "cerrar"]:
            responder(saludo_despedir())
            break

        if texto in comandos_aplicaciones:
            ejecutar(texto)
            continue

        # consultas en línea
        respuesta = buscar_y_abrir(texto)
        responder(respuesta)

    # al cerrar, limpia mixer
    detener()

if __name__ == "__main__":
    main()
