import gradio as gr
from agent.core import MedicalAgent
from data.loader import fetch_med_dialog_sample, format_dialogue_context
import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn

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

# PWA Head Tags
head = """
<link rel="manifest" href="/manifest.json">
<meta name="theme-color" content="#2563eb">
<link rel="apple-touch-icon" href="/icon-192x192.png">
<script>
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('/sw.js')
        .then(reg => console.log('Service Worker registered', reg))
        .catch(err => console.error('Service Worker registration failed', err));
    });
  }
</script>
"""

with gr.Blocks(theme=theme, title="Medical AI Agent", head=head) as demo:
    gr.Markdown(
        """
        # 🏥 Medical AI Assistant
        Powered by **Gemini 3 Flash** and **OpenMed** datasets.
        
        *⚠️ Disclaimer: This is an AI tool for educational purposes. Consult a doctor for medical advice.*
        """
    )
    
    chatbot = gr.ChatInterface(
        fn=medical_chat_interface,
        type="messages",
        examples=["What are common symptoms of iron deficiency?", "Explain hypertension in simple terms."],
        cache_examples=False  # Crucial fix for Hugging Face port conflict
    )

# FastAPI app for serving PWA assets
app = FastAPI()

@app.get("/manifest.json")
async def manifest():
    return FileResponse("pwa_assets/manifest.json")

@app.get("/sw.js")
async def sw():
    return FileResponse("pwa_assets/sw.js", media_type="application/javascript")

@app.get("/icon-192x192.png")
async def icon192():
    return FileResponse("pwa_assets/icon-192x192.png")

@app.get("/icon-512x512.png")
async def icon512():
    return FileResponse("pwa_assets/icon-512x512.png")

# Mount Gradio app
app = gr.mount_gradio_app(app, demo, path="/")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    uvicorn.run(app, host="0.0.0.0", port=port)
