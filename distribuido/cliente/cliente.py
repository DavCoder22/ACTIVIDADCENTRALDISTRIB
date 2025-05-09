import requests
import os

class ClienteConversion:
    def __init__(self, url_servidor):
        self.url_servidor = url_servidor

    def convertir_moneda(self, monto, moneda_destino):
        try:
            response = requests.get(f"{self.url_servidor}/convertir", params={"monto": monto, "moneda_destino": moneda_destino})
            response.raise_for_status()  # Lanza una excepción para errores HTTP
            return response.json()["resultado"]
        except requests.exceptions.RequestException as e:
            print(f"Error al conectar con el servidor: {e}")
            return None
