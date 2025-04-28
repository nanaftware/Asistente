import webbrowser

def buscar_y_abrir(query: str) -> str:
    """
    Abre en el navegador una búsqueda de Google con la consulta dada
    y devuelve un mensaje para el usuario.
    """
    # Formatear la consulta para la URL
    term = query.replace(" ", "+")
    url = f"https://duckduckgo.com/search?q={term}"
    # Abrir el navegador
    webbrowser.open(url)
    # Mensaje para el asistente
    return f"Esto es lo que encontré por «{query}»."
