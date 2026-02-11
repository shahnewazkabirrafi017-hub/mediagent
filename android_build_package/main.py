import flet as ft

def main(page: ft.Page):
    page.title = "MediAgent AI"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 800
    page.padding = 0

    # The most stable URL for mobile embedding
    HF_URL = "https://huggingface.co/spaces/rafi11223/Medi-Agent?embed=true&__theme=light"

    # The WebView component
    webview = ft.WebView(
        HF_URL,
        expand=True,
        javascript_enabled=True,
        on_page_started=lambda _: print("Loading MediAgent..."),
        on_page_ended=lambda _: print("MediAgent Ready!"),
    )

    page.add(webview)

if __name__ == "__main__":
    ft.app(target=main)
