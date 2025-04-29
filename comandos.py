from mensajes import respuestas_comunes

# Listas de comandos
_comandos_aplicaciones = [
    "bloc de notas", "chrome", "brave",
    "whatsapp", "telegram", "spotify", "netflix", "youtube",
    "microsoft edge", "explorador de archivos", "calculadora",
    "apagar computadora", "subir volumen", "bajar volumen"
]

_comandos_detener = ["stop", "detener", "parar"]

# Diccionario único: cada comando → tipo de acción
comandos_dict = {
    **{cmd: "detener" for cmd in _comandos_detener},
    **{cmd: "aplicacion" for cmd in _comandos_aplicaciones}
}

# Acceso a mensaje de no-entendido
NO_ENTENDIDO = respuestas_comunes["no_entendido"]
