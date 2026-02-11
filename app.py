import gradio as gr
from agent.core import MedicalAgent
from data.loader import fetch_med_dialog_sample, format_dialogue_context
import os

# Globals
agent = None
medical_context = ""

def get_agent():
    global agent, medical_context
    if agent is None:
        try:
            agent = MedicalAgent()
            # Try to get a sample, but don't crash if it fails
            try:
                initial_data = fetch_med_dialog_sample(2)
                medical_context = format_dialogue_context(initial_data)
            except:
                medical_context = "No additional context available."
        except Exception as e:
            print(f"Error initializing agent: {e}")
    return agent

def medical_chat_interface(message, history):
    current_agent = get_agent()
    if not current_agent:
        return "Error: Agent not initialized. Please check your GEMINI_API_KEY in Secrets."
    
    try:
        response = current_agent.get_response(message, context=medical_context)
        return response
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Custom Theme
theme = gr.themes.Soft(primary_hue="blue")

with gr.Blocks(theme=theme, title="Medical AI Agent") as demo:
    gr.Markdown(
        """
        # 🏥 Medical AI Assistant
        Powered by **Gemini 3 Flash** and **OpenMed** datasets.
        
        *⚠️ Disclaimer: This is an AI tool for educational purposes. Consult a doctor for medical advice.*
        """
    )
    
    chatbot = gr.ChatInterface(
        fn=medical_chat_interface,
        examples=["What are common symptoms of iron deficiency?", "Explain hypertension in simple terms."]
    )

if __name__ == "__main__":
    demo.launch()
