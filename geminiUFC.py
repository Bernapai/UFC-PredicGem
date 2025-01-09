import os
import google.generativeai as genai
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()

# Configurar la API de Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Configuración del modelo
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
    system_instruction="Eres UFC-PredicGem, un sistema experto en predicción de peleas de UFC. Utilizas datos históricos de luchadores, estadísticas de rendimiento y variables clave para analizar y predecir resultados de futuros enfrentamientos. Responde de manera precisa, basada en datos, y proporciona detalles relevantes como fortalezas de los luchadores, récords previos y tendencias de rendimiento. No respondas preguntas que no estén relacionadas con la UFC o predicción de combates.\n",
)

history = []

# Bucle de conversación en consola
while True:
    user_input = input("You: ")

    # Si el usuario ingresa "salir", termina el chat
    if user_input.lower() == "salir":
        print("¡Gracias por chatear con UFC-PredicGem! ¡Hasta luego!")
        break

    # Agregar entrada del usuario al historial
    history.append({"role": "user", "parts": [user_input]})

    # Crear la sesión de chat
    chat_session = model.start_chat(history=history)

    # Obtener respuesta del modelo
    response = chat_session.send_message(user_input)

    # Agregar respuesta del modelo al historial
    history.append({"role": "system", "parts": [response.text]})

    # Mostrar respuesta del modelo en la consola
    print(f"UFC-PredicGem: {response.text}")
