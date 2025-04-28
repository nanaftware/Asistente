import random

saludos_iniciales = [
    "Hola, soy Nanu tu asistente putona y cariñosa.",
    "¡Hola, papito! ¿En qué puedo ayudarte hoy?",
    "¡Hey! Soy Nanu, tu asistente favorita. ¿Qué necesitas?",
    "¡Hola, te acordaste que existo?",
    "¡Hola, ¿Te cansaste de ver trabas?",
]

saludos_despedida = [
    "¡Hasta luego, papito!",
    "Me voy a mi casita, ¡chao pelotudo!",
    "¡Nos vemos, Amorcito!",
    "¡Me Aburriste Estúpido!",
    "Desconectando... ¡chau te fuiste!",
    "Anda a mirar putas, ¡chao no me hables!",
    "Anda a mirar trabas",
    "¡Anda seguí chamuyando con las putas!",
]

def saludo_inicio():
    return random.choice(saludos_iniciales)

def saludo_despedir():
    return random.choice(saludos_despedida)
