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
        
        # Using Gemini 3 Flash (Latest version in 2026)
        self.model_id = "gemini-3-flash-preview"
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
        
        # Using the simplified generate_content method for standard chat interaction
        response = self.client.models.generate_content(
            model=self.model_id,
            contents=prompt,
            config={
                "system_instruction": self.system_instruction
            }
        )
        return response.text
