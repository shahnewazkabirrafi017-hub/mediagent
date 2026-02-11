---
title: MediAgent
emoji: 🏥
colorFrom: blue
colorTo: slate
sdk: gradio
sdk_version: 5.4.0
pinned: false
---

# Medical AI Agent

A powerful, conversational medical agent built using **Google Gemini 1.5 Flash** and medical datasets from **Hugging Face (OpenMed)**.

## 🚀 Features
- **Conversational Intelligence:** Powered by Gemini 1.5 Flash for high-quality medical reasoning.
- **Data-Driven:** Grounded in real medical dialogues and datasets from the [OpenMed Collection](https://huggingface.co/collections/OpenMed/medical-datasets).
- **Dynamic Updates:** Built-in tools to fetch and integrate new datasets regularly.
- **Web Interface:** Easy-to-use UI built with Gradio.

## 📋 Prerequisites
- Python 3.10+
- Google Gemini API Key (get it from [Google AI Studio](https://aistudio.google.com/))
- Hugging Face Token (if accessing private/restricted datasets)

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shahnewazkabirrafi017-hub/mediagent.git
   cd mediagent
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   Create a `.env` file in the root directory:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   HF_TOKEN=your_huggingface_token_here
   ```

## 🖥️ Usage
Run the application locally:
```bash
python app.py
```

## 📂 Project Structure
- `app.py`: The Gradio web interface.
- `agent/`: Core AI agent logic.
- `data/`: Scripts for dataset management and caching.
- `requirements.txt`: Python package requirements.
- `.env.example`: Template for environment variables.

## 🤝 Contributing
Updates are welcome! Since we plan to regularly add more datasets, feel free to submit pull requests with new data processing scripts.

## ⚠️ Disclaimer
This AI agent is for **educational and research purposes only**. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult with a qualified healthcare provider for medical concerns.
