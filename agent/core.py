import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

class MedicalAgent:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found. Please set it in your environment or .env file.")
        
        genai.configure(api_key=self.api_key)
        
        # Using Gemini 1.5 Flash for speed and generous free tier
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=(
                "You are an advanced Medical AI Assistant. Your goal is to provide accurate, "
                "helpful, and empathetic medical information based on available datasets. "
                "Always maintain a professional tone. "
                "IMPORTANT: You are an AI, not a doctor. Always include a disclaimer that "
                "this information is for educational purposes and the user should consult "
                "a real healthcare professional."
            )
        )
        self.chat = self.model.start_chat(history=[])

    def get_response(self, user_input, context=""):
        prompt = f"User Question: {user_input}\n\nRelevant Medical Context/Data: {context}"
        response = self.chat.send_message(prompt)
        return response.text
