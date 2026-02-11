import flet as ft

def main(page: ft.Page):
    page.title = "Medi-Agent Mobile"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 800
    page.padding = 0

    # Your Hugging Face Space URL
    # Using the embed version ensures the mobile app doesn't show the Hugging Face header
    HF_URL = "https://huggingface.co/spaces/rafi11223/Medi-Agent?embed=true&__theme=light"

    # The WebView component that holds the AI Agent
    webview = ft.WebView(
        HF_URL,
        expand=True,
        javascript_enabled=True,
        on_page_started=lambda _: print("Loading Medi-Agent..."),
        on_page_ended=lambda _: print("Medi-Agent Ready!"),
    )

    page.add(webview)

if __name__ == "__main__":
    ft.app(target=main)
