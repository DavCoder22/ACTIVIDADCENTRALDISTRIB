# Usar una imagen base oficial de Python
FROM python:3.12-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de requisitos y dependencias desde la carpeta principal
COPY ../requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY . .

# Exponer el puerto en el que la aplicación va a correr
EXPOSE 5002

# Comando para correr la aplicación
CMD ["python", "servidor.py"]
