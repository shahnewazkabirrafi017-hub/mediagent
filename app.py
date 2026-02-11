import gradio as gr
from agent.core import MedicalAgent
from data.loader import fetch_med_dialog_sample, format_dialogue_context
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize the agent
# Note: User needs to provide GEMINI_API_KEY in .env
try:
    agent = MedicalAgent()
    # Fetch some initial context to 'prime' the agent
    initial_data = fetch_med_dialog_sample(3)
    medical_context = format_dialogue_context(initial_data)
except Exception as e:
    print(f"Warning: Agent initialization failed (likely missing API key): {e}")
    agent = None
    medical_context = ""

def medical_chat_interface(message, history):
    if not agent:
        return "Error: Agent not initialized. Please ensure GEMINI_API_KEY is set in your .env file."
    
    try:
        response = agent.get_response(message, context=medical_context)
        return response
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Custom Theme for a Professional Medical Look
theme = gr.themes.Soft(
    primary_hue="blue",
    secondary_hue="slate",
    neutral_hue="slate",
    font=[gr.themes.GoogleFont("Inter"), "ui-sans-serif", "system-ui", "sans-serif"],
).set(
    body_background_fill="*neutral_50",
    block_background_fill="white",
    block_border_width="1px",
)

with gr.Blocks(theme=theme, title="Medical AI Agent") as demo:
    gr.Markdown(
        """
        # 🏥 Medical AI Assistant
        Developed by **[shahnewazkabirrafi017-hub](https://github.com/shahnewazkabirrafi017-hub)**
        
        This agent is grounded in the **OpenMed** dataset collection and powered by **Gemini 3 Flash**.
        
        *⚠️ Disclaimer: This is an AI tool for educational purposes. Consult a doctor for medical advice.*
        """
    )
    
    chatbot = gr.ChatInterface(
        fn=medical_chat_interface,
        examples=["What are common symptoms of iron deficiency?", "How can I improve my sleep hygiene?", "Explain what hypertension is in simple terms."]
    )

if __name__ == "__main__":
    demo.launch(theme=theme, share=True)
