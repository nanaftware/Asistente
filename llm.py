# llm.py
import requests

LMSTUDIO_URL = "http://localhost:1234/v1/chat/completions"
HISTORIAL = []

SYSTEM_PROMPT = """Sos Nanu, un asistente virtual en español. 
Respondé de forma breve, clara y amigable. 
Cuando no sepas algo, decilo honestamente."""

def preguntar_al_llm(texto_usuario: str) -> str:
    """Envía el texto al modelo local y devuelve la respuesta."""
    HISTORIAL.append({"role": "user", "content": texto_usuario})

    payload = {
        "model": "nvidia-nemotron-3-nano-4b",  # o el identificador que muestre LM Studio
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT}
        ] + HISTORIAL,
        "max_tokens": 200,
        "temperature": 0.7,
        "stream": False
    }

    try:
        response = requests.post(LMSTUDIO_URL, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        respuesta = data["choices"][0]["message"]["content"].strip()
        HISTORIAL.append({"role": "assistant", "content": respuesta})
        return respuesta
    except requests.exceptions.ConnectionError:
        return "No puedo conectarme al modelo. Verificá que LM Studio esté corriendo."
    except Exception as e:
        return f"Hubo un error al consultar el modelo: {str(e)}"

def limpiar_historial():
    """Reinicia el contexto de la conversación."""
    HISTORIAL.clear()
