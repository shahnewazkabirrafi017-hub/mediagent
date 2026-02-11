import flet as ft

def main(page: ft.Page):
    page.title = "MediAgent AI"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 800
    page.padding = 0

    # The most direct URL to bypass wrappers
    HF_URL = "https://rafi11223-medi-agent.hf.space"

    # Minimal UI with a loading indicator
    loading_text = ft.Text("🏥 Starting Medical Assistant...", size=20, text_align=ft.TextAlign.CENTER)
    
    def on_page_ended(e):
        loading_text.visible = False
        page.update()

    webview = ft.WebView(
        HF_URL,
        expand=True,
        javascript_enabled=True,
        on_page_ended=on_page_ended,
    )

    page.add(
        ft.Column(
            [loading_text, webview],
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
