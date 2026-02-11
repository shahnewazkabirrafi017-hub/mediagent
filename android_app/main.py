import flet as ft

def main(page: ft.Page):
    page.title = "Medi-Agent Mobile"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 800
    page.padding = 0

    # Your Hugging Face Space URL
    # We use the direct "embed" version for a cleaner mobile look
    HF_URL = "https://rafi11223-mediagent.hf.space"

    # Native Mobile UI Components
    def on_window_event(e):
        if e.data == "close":
            page.window_destroy()

    # The WebView component that holds the AI Agent
    webview = ft.WebView(
        HF_URL,
        expand=True,
        on_page_started=lambda _: print("Loading Medi-Agent..."),
        on_page_ended=lambda _: print("Medi-Agent Ready!"),
    )

    page.add(webview)

if __name__ == "__main__":
    # To run locally for testing: flet run android_app/main.py
    # To build APK: flet build apk
    ft.app(target=main)
