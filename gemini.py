import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()


genai.configure(api_key=getenv("GEMINI_API_KEY"))

# Create the model
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
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "jojojoo\n\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "jojojoo! It seems like you're just having some fun with sounds! Is there anything I can help you with? Maybe you'd like me to:\n\n*   **Say it back to you?** (Jojojoo!)\n*   **Try to guess what you mean by it?** (Is it a happy sound? A silly sound?)\n*   **Tell you some fun facts or stories?**\n*   **Answer a question?**\n\nLet me know!\n",
      ],
    },
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)