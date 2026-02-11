from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

class MedicalAgent:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY not found. Please set it in your environment or .env file.")
        
        self.client = Groq(api_key=self.api_key)
        
        # Using Llama 3.3 70B on Groq for ultra-fast, high-quality medical responses
        self.model_id = "llama-3.3-70b-specdec" 
        self.system_instruction = (
            "You are an advanced Medical AI Assistant. Your goal is to provide accurate, "
            "helpful, and empathetic medical information based on available datasets. "
            "Always maintain a professional tone. "
            "IMPORTANT: You are an AI, not a doctor. Always include a disclaimer that "
            "this information is for educational purposes and the user should consult "
            "a real healthcare professional."
        )

    def get_response(self, user_input, context=""):
        try:
            completion = self.client.chat.completions.create(
                model=self.model_id,
                messages=[
                    {"role": "system", "content": self.system_instruction},
                    {"role": "user", "content": f"Context: {context}\n\nQuestion: {user_input}"}
                ],
                temperature=0.7,
                max_tokens=1024,
            )
            return completion.choices[0].message.content
        except Exception as e:
            if "429" in str(e) or "rate_limit" in str(e).lower():
                return "🏥 The Medical Assistant is currently handling many users. Please wait a few moments. (Groq API limit reached)"
            return f"An unexpected error occurred with Groq: {str(e)}"
