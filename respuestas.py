import requests
from bs4 import BeautifulSoup

def buscar_informacion(pregunta):
    """
    Realiza una búsqueda en DuckDuckGo y devuelve un resumen de la información encontrada.
    """
    try:
        # Preparar la consulta
        query = pregunta.replace(' ', '+')
        url = f"https://duckduckgo.com/html/?q={query}"

        # Realizar la solicitud
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Analizar el contenido
        soup = BeautifulSoup(response.text, 'html.parser')
        resultados = soup.find_all('a', class_='result__a', limit=3)

        # Extraer los títulos y enlaces de los primeros resultados
        respuestas = []
        for resultado in resultados:
            titulo = resultado.get_text()
            enlace = resultado['href']
            respuestas.append(f"{titulo} - {enlace}")

        if respuestas:
            return "\n".join(respuestas)
        else:
            return "No se encontraron resultados relevantes."
    except Exception as e:
        return f"Error al buscar información: {e}"
