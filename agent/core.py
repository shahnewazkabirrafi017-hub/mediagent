from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

class MedicalAgent:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found. Please set it in your environment or .env file.")
        
        self.client = genai.Client(api_key=self.api_key)
        
        # Using Gemini 1.5 Flash (Higher free-tier limits: 1,500 requests/day)
        self.model_id = "gemini-1.5-flash"
        self.system_instruction = (
            "You are an advanced Medical AI Assistant. Your goal is to provide accurate, "
            "helpful, and empathetic medical information based on available datasets. "
            "Always maintain a professional tone. "
            "IMPORTANT: You are an AI, not a doctor. Always include a disclaimer that "
            "this information is for educational purposes and the user should consult "
            "a real healthcare professional."
        )

    def get_response(self, user_input, context=""):
        prompt = f"User Question: {user_input}\n\nRelevant Medical Context/Data: {context}"
        
        try:
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=user_input, # Use user_input directly for better context handling
                config={
                    "system_instruction": self.system_instruction
                }
            )
            return response.text
        except Exception as e:
            if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                return "🏥 The Medical Assistant is currently handling many users. Please wait a few moments and try your question again. (Gemini API limit reached)"
            return f"An unexpected error occurred: {str(e)}"
